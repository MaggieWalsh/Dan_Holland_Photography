from django.contrib import admin
from .models import Abouts, Category

# Register your models here.
class AboutsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'about_image',
        'about_description',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )



admin.site.register(Abouts, AboutsAdmin)
admin.site.register(Category, CategoryAdmin)