# Generated by Django 2.0.13 on 2020-11-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_offer_ongoing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]
