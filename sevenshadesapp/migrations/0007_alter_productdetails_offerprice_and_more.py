# Generated by Django 5.0.2 on 2024-04-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevenshadesapp', '0006_rename_productdid_productdetails_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='offerprice',
            field=models.IntegerField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.IntegerField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='qty',
            field=models.IntegerField(default='', max_length=70),
        ),
    ]