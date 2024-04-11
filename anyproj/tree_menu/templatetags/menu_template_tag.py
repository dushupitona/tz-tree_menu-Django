from django import template
from tree_menu.models import MenuItemModel


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def show_menu():
    data = MenuItemModel.objects.values_list().order_by("lvl")
    print(data)
    return {'one': 1}



# menu_name = 'Fruits'
# menu_json ={
#     'branch_1': {
#         'name': 'fruits',
#         'url': 'http://fruits/',
#         'lvl_1': {

#             'branch_1': {
#                 'name': 'mango',
#                 'url': 'http://fruits/mango/'
#             },

#             'branch_2': {
#                 'name': 'apples',
#                 'url': 'http://fruits/apple/',
#                 'lvl_2': {

#                     'branch_1': {
#                         'name': 'red',
#                         'url': 'http://fruits/apple/red/'
#                     },

#                     'branch_2': {
#                         'name': 'green',
#                         'url': 'http://fruits/apple/green/'
#                     },
#                 }
#             },
#         }
#     },

#     'branch_2': {
#         'name': 'vegetables',
#         'url': 'http://vegetables/'
#     },
    
# }