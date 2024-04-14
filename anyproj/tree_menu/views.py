from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tree_menu/index.html')

def fruits_index(request, slug):
    return render(request, 'slug_index.html', context={'slug': slug})


def test_index(request):
    return render(request, )