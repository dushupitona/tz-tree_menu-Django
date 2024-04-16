from django.urls import path

from tree_menu.views import product_index, end_index

app_name = 'tree_menu'

urlpatterns = [
    path('fruits/', product_index, name='fruits'),
    path('vegetables/', product_index, name='vegetables'),
    path('caviar/', end_index, name='caviar'),
    path('fruits/apples/', product_index, name='apples'),
    path('fruits/oranges/', product_index, name='oranges'),
    path('fruits/oranges/red_orange', end_index, name='red_orange'),
    path('fruits/mango/', product_index, name='mango'),
    path('fruits/apples/red_apple/', product_index, name='red_apple'),
    path('fruits/apples/green_apple/', product_index, name='green_apple'),
    path('fruits/mango/gold_mango/', end_index, name='gold_mango'),
    path('vegetables/cucumber/', product_index, name='cucumber'),
    path('fruits/apples/red_apple/red_apple_in_lenta/', end_index, name='red_apple_in_lenta'),
    path('fruits/apples/red_apple/green_apple_in_lenta/', end_index, name='green_apple_in_lenta'),
    path('vegetables/cucumber/smooth_cucumber', end_index, name='smooth_cucumber'),


    path('sport/', product_index, name='sport'),
    path('sport/audi', end_index, name='audi'),
    path('sport/ferarri', end_index, name='ferarri'),
    path('usual/', product_index, name='usual'),
    path('usual/lada', end_index, name='lada'),

]
