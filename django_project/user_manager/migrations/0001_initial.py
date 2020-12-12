# Generated by Django 3.1.4 on 2020-12-11 15:52

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):
    initial = True
    
    dependencies = [
    ]
    
    operations = [
        migrations.CreateModel(
                name = 'Product',
                fields = [
                    ('created_at', models.DateTimeField(auto_now_add = True)),
                    ('updated_at', models.DateTimeField(auto_now = True)),
                    ('id', models.AutoField(primary_key = True, serialize = False)),
                    ('name', models.CharField(max_length = 50, verbose_name = 'Название товара')),
                    ('photo', models.CharField(max_length = 200, verbose_name = 'Фото file_id')),
                    ('price', models.DecimalField(decimal_places = 2, max_digits = 8, verbose_name = 'Цена')),
                    ('description', models.TextField(max_length = 3000, null = True, verbose_name = 'Описание')),
                ],
                options = {
                    'verbose_name':'Товар',
                    'verbose_name_plural':'Товары',
                },
        ),
        migrations.CreateModel(
                name = 'User',
                fields = [
                    ('created_at', models.DateTimeField(auto_now_add = True)),
                    ('updated_at', models.DateTimeField(auto_now = True)),
                    ('id', models.AutoField(primary_key = True, serialize = False)),
                    ('user_id',
                     models.BigIntegerField(default = 1, unique = True, verbose_name = 'ID Пользователя Телеграм')),
                    ('name', models.CharField(max_length = 100, verbose_name = 'Имя пользователя')),
                    ('username', models.CharField(max_length = 100, null = True, verbose_name = 'Username Телеграм')),
                    ('email', models.CharField(max_length = 100, null = True, verbose_name = 'Email')),
                    ('bonus', models.DecimalField(decimal_places = 2, max_digits = 8, verbose_name = 'Бонус')),
                ],
                options = {
                    'verbose_name':'Пользователь',
                    'verbose_name_plural':'Пользователи',
                },
        ),
        migrations.CreateModel(
                name = 'Purchase',
                fields = [
                    ('created_at', models.DateTimeField(auto_now_add = True)),
                    ('updated_at', models.DateTimeField(auto_now = True)),
                    ('id', models.AutoField(primary_key = True, serialize = False)),
                    ('amount', models.DecimalField(decimal_places = 2, max_digits = 8, verbose_name = 'Стоимость')),
                    ('quantity', models.IntegerField(verbose_name = 'Количество')),
                    ('shipping_address', jsonfield.fields.JSONField(null = True, verbose_name = 'Адрес Доставки')),
                    ('payed', models.BooleanField(default = False, verbose_name = 'Оплачено')),
                    ('buyer', models.ForeignKey(on_delete = models.SET(0), to = 'user_manager.user',
                                                verbose_name = 'Покупатель')),
                    ('product_id',
                     models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = 'user_manager.product',
                                       verbose_name = 'Идентификатор Товара')),
                ],
                options = {
                    'verbose_name':'Покупка',
                    'verbose_name_plural':'Покупки',
                },
        ),
    ]
