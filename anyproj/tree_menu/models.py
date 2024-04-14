from django.db import models    

# Create your models here.

class MenuModel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class MenuItemModel(models.Model):
    menu = models.ForeignKey(to=MenuModel, on_delete=models.CASCADE)
    slug = models.SlugField()
    name = models.CharField(max_length=64)
    lvl = models.IntegerField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='parent_go',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    


    
    # m.objects.values_list('name', 'parent__name', 'parent__parent__name', 'parent__parent__parent__name' ) 


    # from tree_menu.models import MenuItemModel as m

    # need slug !!!