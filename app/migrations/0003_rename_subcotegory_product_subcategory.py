# Generated by Django 4.1.2 on 2022-10-31 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='subcotegory',
            new_name='subcategory',
        ),
    ]
