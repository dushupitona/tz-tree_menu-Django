from django.urls import path

from tree_menu.views import fruits_index

app_name = 'tree_menu'

urlpatterns = [
    path('<slug:slug>/', fruits_index, name='fruits_go' )
]
