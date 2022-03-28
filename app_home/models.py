from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.

class categ(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    logo = models.ImageField(upload_to="Menubar_brand_log", default='')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categoties'

    def get_url(self):
        return reverse('prod_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    model_img = models.ImageField(upload_to='product', default='')
    extra_reduce_amount = models.CharField(max_length=100, default='')
    off_prize = models.CharField(max_length=20, default='')
    off_prize2 = models.CharField(max_length=20, default='')
    percentage_off = models.CharField(max_length=100, default='')
    brand = models.ImageField(upload_to='brand logo', default='')
    mobile_feature1 = models.TextField(default='')
    mobile_feature2 = models.TextField(default='')
    mobile_feature3 = models.TextField(default='')
    mobile_feature4 = models.TextField(default='')
    product_desc = models.TextField(default='')
    camera_img = models.ImageField(upload_to='camera quality images', default='')
    mega_pixel = models.CharField(max_length=200, default='')
    MP_description = models.TextField(default='')
    display = models.CharField(max_length=100, default='')
    display_desc = models.TextField(default='')

    # -----------GENERAL---------------

    in_the_box = models.TextField(default='')
    model_number = models.CharField(max_length=100, default='')
    color = models.CharField(max_length=50, default='')
    browse_type = models.CharField(max_length=100, default='')
    sim_type = models.CharField(max_length=50, default='')
    model_RAM = models.ImageField(default='')
    model_ROM = models.ImageField(default='')
    stock = models.IntegerField()
    available = models.BooleanField()
    category = models.ForeignKey(categ, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
