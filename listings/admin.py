from django.contrib import admin
from .models import Listings

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('title','infr','price','is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    list_per_page = 3
    
admin.site.register(Listings,ListingsAdmin)


