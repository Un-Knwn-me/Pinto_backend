# Generated by Django 5.1.2 on 2024-11-13 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_category_cuisine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuisine',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
    ]
