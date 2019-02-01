from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'listing', 'listing_id', 'contact_date', 'user_id')   
    list_display_links=('id','name','listing') 
    search_fields = ('name', 'listing', 'email')    
    list_per_page =10


# Register your models here.
admin.site.register(Contact, ContactAdmin)
