from django import template
from tree_menu.models import MenuItemModel, MenuModel

import pprint


register = template.Library()

    
@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    response_dict = MenuItemModel.objects.select_related('menu').filter(menu__name=menu_name).values('slug', 'lvl', 'name', 'parent__slug', 'menu__name')

    current_page_url = context['request'].path

    current_page_url = current_page_url.split('/')

    print(current_page_url)

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


    def remove_indices(lst, indices):
        return [val for i, val in enumerate(lst) if i not in indices]
    

    def cut_by_url(out_list, url):
        if url == ['', '']:
            new_out = []
            for set in out_list:
                if set[1] == 0:
                    new_out.append(set)
        else:
            new_out = out_list
            rem_index = []
            for set in out_list:
                print(f'{set} | {url} | {set[0] in url}')
                if set[0] not in url and set[1]!=0 and set[2] not in url:
                    rem_index.append(out_list.index(set))
            new_out = remove_indices(new_out, rem_index)
        
        print(new_out)

        return new_out

    out = cut_by_url(out, current_page_url)

    # pprint.pprint(out)
    context = {'out_data': out}     
    return context