from django.urls import path

from tree_menu.views import index

app_name = 'tree_menu'

urlpatterns = [
    path('fruits/', index, name='fruits'),
    path('vegetables/', index, name='vegetables'),
    path('fruits/apples/', index, name='apples'),
    path('no_matter_what_url', index, name='oranges'),
    path('fruits/mango/', index, name='mangooo'),
    path('fruits/apples/red_apple/', index, name='red_apple'),
    path('fruits/apples/green_apple/', index, name='green_apple'),
    path('vegetables/pepper/', index, name='pepper'),


    path('sport/', index, name='sport'),
    path('sport/audi', index, name='audi'),
    path('usual/', index, name='usual'),
    path('usual/lada', index, name='lada'),

]
