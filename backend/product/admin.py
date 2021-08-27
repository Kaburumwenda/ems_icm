from django.contrib import admin
from .models import *
# Register your models here.

from import_export.admin import ImportExportModelAdmin

from import_export import resources

@admin.register(Fakedata)
class DataAdmin(ImportExportModelAdmin):
    pass



class ProductAdmin(admin.ModelAdmin):
    list_display=['title', 'category']
    # prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields = {'slug': ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields = {'slug': ('name',)}


class MenuAdmin(admin.ModelAdmin):
    list_display=['title']
    prepopulated_fields = {'slug': ('title',)}


class SubMenuAdmin(admin.ModelAdmin):
    list_display=['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(menuEntries)
admin.site.register(submenu)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)