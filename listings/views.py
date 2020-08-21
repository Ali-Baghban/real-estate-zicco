from django.shortcuts import render,get_object_or_404
from .models import Listings

def index(request):
    listings    = Listings.objects.all()
    #count      = Listings.objects.all().count()
    context     = {
        'listings': listings,
    }
    return render(request, 'listings/index.html', context=context )
    
def details(request,listing_id):
    listing = get_object_or_404(Listings,id=listing_id)
    context = {'listing':listing,}
    return render(request,'listings/details.html', context=context)

def search(request):
    listings = Listings.objects.all()
    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        print(bedroom)
        listings = listings.filter(bedroom=bedroom)
    context     = {
        'listings': listings,
    }
    return render(request, 'listings/index.html', context=context )    

