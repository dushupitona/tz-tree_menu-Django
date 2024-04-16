from django.urls import path

from tree_menu.views import product_index, product_index

app_name = 'tree_menu'

urlpatterns = [
    path('fruits/', product_index, name='fruits'),
    path('vegetables/', product_index, name='vegetables'),
    path('fruits/apples/', product_index, name='apples'),
    path('fruits/oranges/', product_index, name='oranges'),
    path('fruits/mango/', product_index, name='mango'),
    path('fruits/apples/red_apple/', product_index, name='red_apple'),
    path('fruits/apples/green_apple/', product_index, name='green_apple'),
    path('vegetables/pepper/', product_index, name='pepper'),


    path('sport/', product_index, name='sport'),
    path('sport/audi', product_index, name='audi'),
    path('sport/ferarri', product_index, name='ferarri'),
    path('usual/', product_index, name='usual'),
    path('usual/lada', product_index, name='lada'),

]
