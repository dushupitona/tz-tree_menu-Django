from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class MenuModel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class MenuItemModel(models.Model):
    menu = models.ForeignKey(to=MenuModel, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64)
    lvl = models.IntegerField(validators=[MinValueValidator(0)])
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    url = models.URLField(blank=True)
    named_url = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    