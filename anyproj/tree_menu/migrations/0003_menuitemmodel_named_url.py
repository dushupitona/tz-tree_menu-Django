# Generated by Django 5.0.4 on 2024-04-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_menuitemmodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitemmodel',
            name='named_url',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
