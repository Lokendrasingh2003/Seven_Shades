# Generated by Django 5.0.2 on 2024-04-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevenshadesapp', '0010_adminlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerdescription', models.CharField(default='', max_length=70)),
                ('pictures', models.ImageField(upload_to='static/')),
            ],
        ),
    ]