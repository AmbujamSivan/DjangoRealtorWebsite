from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator,Page
from . models import Listing

from .choices import price_choices, bedroom_chices,state_choices


# Clistings views- funct def.
def index(request):
   # Ordering the list based on list date desc and filtering the unpublished
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)

   #pagination setup ref django doc for details
   paginator = Paginator(listings, 6)
   page = request.GET.get('page')
   paged_listing = paginator.get_page(page)

   context = {
      'listings' : paged_listing
   }
   return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
   listing = get_object_or_404(Listing, pk=listing_id)
   context ={
      'listing' : listing
   }
   return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #search by keywords: __icontains eq if para has the word
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
         queryset_list = queryset_list.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
      city = request.GET['city']
      if city:
         queryset_list = queryset_list.filter(city__iexact=city)
    # state
    if 'state' in request.GET:
      state = request.GET['state']
      if state:
         queryset_list = queryset_list.filter(state__iexact=state)
    # Bedrooms -less tahn or equal to :lte
    if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    # price
    if 'price' in request.GET:
      price = request.GET['price']
      if price:
         queryset_list = queryset_list.filter(price__lte=price)

    context = {
         'listings' : queryset_list,
         'state_choices' : state_choices,
         'bedroom_choices' : bedroom_chices,
         'price_choices' : price_choices,
         'values' : request.GET
         }
    return render(request,'pages/index.html', context)

    return render(request, 'listings/search.html')