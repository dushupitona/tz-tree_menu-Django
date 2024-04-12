from django import template
from tree_menu.models import MenuItemModel, MenuModel


register = template.Library()

    
@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(menu_name):
    # # data = MenuItemModel.objects.select_related('menu').filter(menu=args).values_list().order_by("lvl")
    # print(MenuModel.objects.get(name=menu_name).menuitemmodel_set.values_list())
    response_dict = MenuItemModel.objects.select_related('menu').filter(menu__name='red_menu').values('slug', 'name', 'parent__slug', 'menu__name')
    
    context = {
        'out_data': response_dict
    }

    return context

    # query = [
    #  ('Fuits', 0, 'fruits', None),
    #  ('Vegetables', 0, 'vegetables', None),
    #  ('Apples', 1, 'apples', 'fruits'),
    #  ('Mango', 1, 'mango', 'fruits'),
    #  ('Red apple', 2, 'red_apple', 'apples'),
    #  ('Green apple', 2, 'green_apple', 'apples')
    #  ]
    

    
