from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_header = "Pillow Mart"

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')
    list_display_links = ('id', 'username')

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Department)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    inlines = [
        CategoryInline
    ]
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_photo')
    list_display_links = ('name',)
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {'slug': ('name',)}
    
    def get_photo(self, product):
        images = product.productimage_set.all()
        if images:
            return mark_safe(f'<img src="{images[0].photo.url}" width="20%">')

