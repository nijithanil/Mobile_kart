from django.contrib import admin
from .models import *


# Register your models here.

class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # list_display = ['name', 'slug', 'logo']
    # lisi_editable = ['name', 'slug', 'logo']


admin.site.register(categ, catagdmin)


class prodAdmin(admin.ModelAdmin):
    # list_display = ['model_img']
    # list_editable = ['model_img']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(products, prodAdmin)
