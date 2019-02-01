from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def login(request):# post login page
    if request.method == 'POST':
        username = request.POST['username']        
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)            
            messages.success(request,'you are successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username/password-login failed')
            return redirect('login')
    else:# get loging page
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you are successfully logged out')
        return redirect('index')
    
def register(request):
    if request.method == 'POST':
        #getting form values- messages.error(request,'Testing error message')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # validation
        if password == password2:
            # check user in db
            if User.objects.filter(username=username).exists():
               messages.error(request,'user name already exist/taken') 
               return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email is already registered') 
                    return redirect('register')
                else:
                    # looks good- auth.login(request,user)
                    user =User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    #One way of doing is to login the user after creation 
                    # auth.login(request,user)
                    # messages.success(request,'You ar now logged in')
                    # return redirect('index')
                    
                    messages.success(request,'You are now registered you can log in now')
                    return  redirect('login')
        else:
            messages.error(request,'paswords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
    
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
        }
    return render(request, 'accounts/dashboard.html',context)
    
    