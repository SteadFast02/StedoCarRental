# Generated by Django 4.1.5 on 2023-04-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalSystemApp', '0003_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(default='', max_length=70)),
                ('mobileno', models.CharField(default='', max_length=15)),
                ('emailid', models.CharField(default='', max_length=150)),
                ('password', models.CharField(default='', max_length=150)),
                ('adminpic', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
