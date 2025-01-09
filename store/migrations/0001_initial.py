# Generated by Django 5.1.4 on 2025-01-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание категории')),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение категории')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='название продукта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание продукта')),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('first_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='1-ое изображение продукта')),
                ('second_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='2-ое изображение продукта')),
                ('third_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='3-ое изображение продукта')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('product_name',),
            },
        ),
    ]
