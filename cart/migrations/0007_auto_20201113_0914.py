# Generated by Django 3.1.3 on 2020-11-13 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20201113_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order_details',
            options={'verbose_name_plural': 'Order details'},
        ),
        migrations.RenameField(
            model_name='order_details',
            old_name='city',
            new_name='country',
        ),
    ]
