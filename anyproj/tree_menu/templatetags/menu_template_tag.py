from django import template
from tree_menu.models import MenuItemModel


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def show_menu():
    data = MenuItemModel.objects.values_list().order_by("lvl")

    
    

    query = [
     ('Fuits', 0, 'fruits', None),
     ('Vegetables', 0, 'vegetables', None),
     ('Apples', 1, 'apples', 'fruits'),
     ('Mango', 1, 'mango', 'fruits'),
     ('Red apple', 2, 'red_apple', 'apples'),
     ('Green apple', 2, 'green_apple', 'apples')
     ]
    

    




    # a = {}

    # for tup in query:
    #     a[tup[2]] = {
    #         'name': tup[0],
    #         'lvl': tup[1],
    #         'parent': tup[3]}   
        

    # {
    #  'fruits': {'name': 'Fuits', 'lvl': 0, 'parent': None},
    #  'vegetables': {'name': 'Vegetables', 'lvl': 0, 'parent': None},
    #  'apples': {'name': 'Apples', 'lvl': 1, 'parent': 'fruits'},
    #  'mango': {'name': 'Mango', 'lvl': 1, 'parent': 'fruits'},
    #  'red_apple': {'name': 'Red apple', 'lvl': 2, 'parent': 'apples'},
    #  'green_apple': {'name': 'Green apple', 'lvl': 2, 'parent': 'apples'}
    # }




    

    

        
                    



        # branch_count = 0

    # for tup in query:
    #     if tup[1] == 0:
    #         branch_count+=1
    #         menu_dict['branch_' + str(branch_count)]= {'parent_slug': tup[2]}
    #     else:
    #         for key, value in menu_dict.items():
    #             if tup[2 + tup[1]] == value['parent_slug']:
    #                 value['lvl_' + str(tup[1])] = {
    #                     'name': tup[0],
    #                     'slug': tup[2]
    #                 }                


        
            
        # {
        #     'branch_1':
        #         {
        #             'parent_slug': 'fruits',
        #             'children': {}
        #         },

        #     'branch_2':
        #         {
        #             'parent_slug': 'vegetables',
        #             'children': {}
        #             }
        # }
    
    data = {'one': 1, 'two': 2}
        
    return data












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