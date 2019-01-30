from django.contrib import admin
from .models import Listing

 #to enable link based on the below identified filed  
 # to display the listed field as grid in listing view
class ListingAdmin(admin.ModelAdmin):
    
    list_display= ('id','title','is_published','price','list_date','realtor')   
    list_display_links=('id','title','realtor')      
    list_filter = ('realtor',)    
    list_editable = ('is_published',)
    search_fields = ('id', 'address', 'state', 'zipcode','title','city')
    list_per_page = 3

# Register your models here.
admin.site.register(Listing, ListingAdmin)
