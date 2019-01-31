from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

from listings.choices import price_choices, bedroom_chices,state_choices

#View for Index page
def index(request):
    #return HttpResponse('<h1>"This is a page"</h1>')
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
         'listings' : listings,
         'state_choices' : state_choices,
         'bedroom_choices' : bedroom_chices,
         'price_choices' : price_choices
         }
    return render(request,'pages/index.html', context)

def about(request):
     realtors = Realtor.objects.order_by('-hire_date')
     # getting the seller of the month
     mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

     context = {
          'realtors': realtors,
          'mvp_realtors': mvp_realtors
     }
     return render(request,'pages/about.html', context)