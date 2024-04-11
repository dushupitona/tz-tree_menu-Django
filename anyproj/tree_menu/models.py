from django.db import models
from tree_menu.manager import MenuQuerySet

# Create your models here.

class MenuItemModel(models.Model):
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

    objects = MenuQuerySet.as_manager()

    def __str__(self):
        return self.name
    


    
    # m.objects.values_list('name', 'parent__name', 'parent__parent__name', 'parent__parent__parent__name' ) 


    # from tree_menu.models import MenuItemModel as m

    # need slug !!!