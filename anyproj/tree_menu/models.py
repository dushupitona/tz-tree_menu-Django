from django.db import models    

# Create your models here.

class MenuModel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class MenuItemModel(models.Model):
    menu = models.ForeignKey(to=MenuModel, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64)
    lvl = models.IntegerField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    url = models.URLField(blank=True)
    named_url = models.SlugField()

    def __str__(self):
        return self.name
    