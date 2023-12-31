# Generated by Django 4.2.5 on 2023-10-31 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scrubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XXL', 'XXL'), ('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S'), ('XS', 'XS')], max_length=200)),
                ('color', models.CharField(blank=True, choices=[('Blue', 'Blue'), ('Pink', 'Pink'), ('Black', 'Black'), ('Light-blue', 'Light-Blue'), ('Red', 'Red'), ('Green', 'Green')], max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='')),
                ('is_new', models.BooleanField(default=False)),
            ],
        ),
    ]
