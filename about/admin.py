from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    """ Admin fields """
    list_display = ('about_image', 'about_description',)


admin.site.register(About, AboutAdmin)