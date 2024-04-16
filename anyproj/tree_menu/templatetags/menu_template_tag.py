from django import template
from tree_menu.models import MenuItemModel
from django.http import HttpRequest 
from django.urls import resolve


register = template.Library()

    
@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    response_dict = MenuItemModel.objects.select_related('menu').filter(menu__name=menu_name).values('slug', 'lvl', 'name', 'parent__slug', 'url', 'named_url')

    current_page_url = context['request'].path

    slug_list = []
    [slug_list.append((dct['slug'], dct['lvl'], dct['url'], dct['named_url'], dct['name'], dct['parent__slug'] if dct['parent__slug'] is not None else 'parent')) for dct in response_dict]
    slug_list = sorted(slug_list, key=lambda x: (x[1], x[2]))

    def get_slug_by_url(url, slug_list):
        request = HttpRequest()
        request.path = url
        matched_view = resolve(request.path)
        url_name =  matched_view.url_name
        
        for set in slug_list:
            if set[3] == url_name:
                return set
        return 'main_page'
    
    out = []

    def add_set(set):
        lvl = set[1]
        parent = set[5]

        if lvl == 0:
            out.append(set)
        else:
            for ad_set in out:
                if ad_set[0] == parent:
                    index = out.index(ad_set)+1
                    out.insert(index, set)

    for set in slug_list:
        add_set(set)

    def cut_by_url(out_list):
        current_set = get_slug_by_url(current_page_url, slug_list)
        if current_set == 'main_page':
            new_out = []
            for set in out_list:
                if set[1] == 0:
                    new_out.append(set)

        elif current_set[1] == 0:
            new_out = []
            for set in out_list:
                if set[1] == 0 or set[5] == current_set[0]:
                    new_out.append(set)

        else:
            new_out = []
            for x in range(len(out_list)):
                if out_list[x][1] == 0:
                    new_out.append(out_list[x])
                else:
                    need_add = []
                    if out_list[x][0] == current_set[0]:
                        ind = x
                        k = current_set[1]
                        for _ in range(ind, 0, -1):
                            if out_list[_][1] <= k and k!=0:
                                 k-=1
                                 need_add.append(out_list[_])

                    elif out_list[x][5] == current_set[0]:
                        need_add.append(out_list[x])
                           
                    for set in need_add[::-1]:
                        new_out.append(set)   

        return new_out

    out = cut_by_url(out)

    context = {'out_data': out}     
    return context