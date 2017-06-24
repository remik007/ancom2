from django.contrib import admin
from .models import Category, Product, Type, Slider


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Slider)