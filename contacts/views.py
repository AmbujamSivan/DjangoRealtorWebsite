from django.shortcuts import render,redirect
from django.contrib import messages
#from django.core.mail import send_mail
#from django.core.mail import EmailMessage

from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST['listing']
        
        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        # check if the user has made the inquiry already
        if request.user.is_authenticated:
            user_id= request.POST['user_id']
            realtor_email = request.POST['realtor_email']
            has_contacted =Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        # save inquires even if user is logged in or not        
        contact.save()       
        
        #send mail
        # send_mail(
        #     'Property Listing Inquiry'
        #     'There has been an inquiry for'+ listing +'. Signin to admin panel for more info'
        #     'aumbujaum@gmail.com'
        #     [realtor_email,'aumbujaum@gmail.com'],
        #     fail_silently=False
        #       )
        # email = EmailMessage('title', 'body', to=[email])
        # email.send()
        
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon!')
        return redirect('/listings/'+listing_id)
