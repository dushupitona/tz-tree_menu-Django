from django import template
from tree_menu.models import MenuItemModel, MenuModel

import pprint


register = template.Library()

    
@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    response_dict = MenuItemModel.objects.select_related('menu').filter(menu__name=menu_name).values('slug', 'lvl', 'name', 'parent__slug', 'menu__name')


    slug_set = []
    [slug_set.append((dct['slug'], dct['lvl'], dct['parent__slug'] if dct['parent__slug'] is not None else 'parent')) for dct in response_dict]
    slug_set = sorted(slug_set, key=lambda x: (x[1], x[2]))

    # [('fruits', 0, 'parent'), ('vegetables', 0, 'parent'), ('apples', 1, 'fruits'), ('mango', 1, 'fruits'), ('cucumber', 1, 'vegetables'), ('red_apple', 2, 'apples'), ('green_apple', 2, 'apples'), ('gold_mango', 2, 'mango')]


    out = []

    def add_set(set):
        slug = set[0]
        lvl = set[1]
        parent = set[2]

        if lvl == 0:
            out.append(set)
        else:
            for ad_set in out:
                if ad_set[0] == parent:
                    index = out.index(ad_set)+1
                    out.insert(index, set)


    for set in slug_set:
        add_set(set)

    pprint.pprint(out)
    context = {'out_data': out} 
    return context