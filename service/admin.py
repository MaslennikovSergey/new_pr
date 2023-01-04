from django.contrib import admin
from .models import Product, Bin, Home

# Register your models here.

#admin.site.register(Product)
admin.site.register(Bin)

@admin.register(Product)  # декоратор с указанием модели

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'cost', 'is_active']
    fields = ['id']
    list_filter = ['cost']
    search_fields = ['']

#admin.site.register(Product, admin.site.register(Product))

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    
    list_display = ['size', 'cost', 'adr', 'bal']
    #fields = ['id']
    #list_filter = ['cost']
    #search_fields = ['']
