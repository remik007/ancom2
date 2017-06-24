from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField


class School_Services(models.Model):
    description = models.TextField(null=True)
    def __str__(self):
        return self.description

class Company_Services(models.Model):
    description = models.TextField(null=True)
    def __str__(self):
        return self.description

class IT_Services(models.Model):
    description = models.TextField(null=True)
    def __str__(self):
        return self.description

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image_thumbnail = ResizedImageField(size=[1600, 700], crop=['middle', 'center'], null=True, blank=True)
    first = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200)
    last_modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Typ'
        verbose_name_plural = 'Typy'

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='productcategory')
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, related_name='producttype', null=True, blank=True)
    company = models.CharField(max_length=200,null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    image_thumbnail = ResizedImageField(size=[400, 250], crop=['middle', 'center'], null=True, blank=True)
    short_description = models.CharField(max_length=500,null=True, blank=True)
    full_description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    available = models.BooleanField(default=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
        ordering = ('type','name',)


    def __str__(self):
        return self.name


