# Generated by Django 3.2.8 on 2021-10-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211028_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_data',
            name='company_image',
            field=models.ImageField(default='DEFAULT VALUE', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='DEFAULT VALUE', null=True, upload_to='images/'),
        ),
    ]
