from django.contrib import admin
from .models import *


# Register your models here.

class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'logo']
    lisi_editable = ['logo']


admin.site.register(categ, catagdmin)


class prodAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'model_img', 'brand', 'brand_image', 'stock', 'available']
    list_editable = ['model_img', 'brand', 'brand_image', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(products, prodAdmin)
