# Generated by Django 5.0.4 on 2024-04-16 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0004_alter_menuitemmodel_slug_alter_menuitemmodel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemmodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menuitemmodel'),
        ),
        migrations.AlterField(
            model_name='menuitemmodel',
            name='url',
            field=models.URLField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
