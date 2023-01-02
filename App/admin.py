from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    search_fields = ['name', 'email', 'subject']
    list_per_page = 3
    

admin.site.register(Contact, ContactAdmin)