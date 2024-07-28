# Generated by Django 5.0.2 on 2024-03-31 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevenshadesapp', '0004_rename_mysubcategoryid_product_subcategoryid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productsubname', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=150)),
                ('qty', models.CharField(default='', max_length=70)),
                ('price', models.CharField(default='', max_length=70)),
                ('color', models.CharField(default='', max_length=70)),
                ('size', models.CharField(default='', max_length=70)),
                ('offerprice', models.CharField(default='', max_length=70)),
                ('offertype', models.CharField(default='', max_length=70)),
                ('icon', models.ImageField(upload_to='static/')),
                ('brandid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sevenshadesapp.brands')),
                ('maincategoryid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sevenshadesapp.maincategory')),
                ('productdid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sevenshadesapp.product')),
                ('subcategoryid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sevenshadesapp.mysubcategory')),
            ],
        ),
    ]
