from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Admin fields """
    list_display = ('email_date', 'enquiry', 'order_number', 'user',)
    ordering = ('-email_date', 'user',)


admin.site.register(Contact, ContactAdmin)