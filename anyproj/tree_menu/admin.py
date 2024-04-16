from django.contrib import admin

from tree_menu.models import MenuItemModel, MenuModel

# Register your models here.


@admin.register(MenuModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(MenuItemModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'named_url', 'url']
