# Generated by Django 4.1.5 on 2023-04-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalSystemApp', '0002_subcategory_alter_category_categoryname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.CharField(default='', max_length=100)),
                ('subcategoryid', models.CharField(default='', max_length=100)),
                ('modelyear', models.CharField(default='', max_length=170)),
                ('variant', models.CharField(default='', max_length=170)),
                ('price', models.CharField(default='', max_length=170)),
                ('insured', models.CharField(default='', max_length=70)),
                ('registrationno', models.CharField(default='', max_length=170)),
                ('ownername', models.CharField(default='', max_length=170)),
                ('mobileno', models.CharField(default='', max_length=170)),
                ('color', models.CharField(default='', max_length=170)),
                ('fueltype', models.CharField(default='', max_length=170)),
                ('numofseats', models.CharField(default='', max_length=170)),
                ('transmissiontype', models.CharField(default='', max_length=170)),
                ('vehicleicon', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
