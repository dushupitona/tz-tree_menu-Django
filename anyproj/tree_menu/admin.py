from django.contrib import admin

from tree_menu.models import MenuItemModel, MenuModel

# Register your models here.


admin.site.register(MenuItemModel)
admin.site.register(MenuModel)