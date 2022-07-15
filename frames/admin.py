from django.contrib import admin
from .models import Frame, Category

# Register your models here.

class FrameAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Frame, FrameAdmin)
admin.site.register(Category, CategoryAdmin)