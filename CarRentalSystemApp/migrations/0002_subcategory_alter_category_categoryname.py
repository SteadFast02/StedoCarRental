# Generated by Django 4.1.5 on 2023-04-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalSystemApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.CharField(default='', max_length=70)),
                ('companyname', models.CharField(default='', max_length=70)),
                ('subcategoryname', models.CharField(default='', max_length=70)),
                ('subcategorydescription', models.CharField(default='', max_length=150)),
                ('subcategoryicon', models.ImageField(upload_to='static/')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
