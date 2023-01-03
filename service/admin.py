from django.contrib import admin
from .models import Product, Bin

# Register your models here.

#admin.site.register(Product)
admin.site.register(Bin)

@admin.register(Product)  # декоратор с указанием модели

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'cost']
    fields = ['id']
    list_filter = ['cost']
    search_fields = ['']

#admin.site.register(Product, admin.site.register(Product))
