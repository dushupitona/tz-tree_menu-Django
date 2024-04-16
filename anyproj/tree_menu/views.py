from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tree_menu/index.html')

def product_index(request):
    return render(request, 'slug_index.html')


def end_index(request):
    return render(request, 'end_index.html')

def car_index(request):
    return render(request, 'tree_menu/index.html')