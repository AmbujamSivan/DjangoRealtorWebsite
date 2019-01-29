from django.shortcuts import render

# Clistings views- funct def.
def index(request):
   return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')