# Generated by Django 2.0.13 on 2020-11-10 09:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201107_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_detail',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
