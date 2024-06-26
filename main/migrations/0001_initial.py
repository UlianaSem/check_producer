# Generated by Django 5.0.4 on 2024-04-21 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100, unique=True, verbose_name='Идентификатор')),
                ('timestamp', models.DateTimeField(verbose_name='Дата и время')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Общая сумма чека')),
                ('nds_amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Сумма НДС')),
                ('tips_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Сумма чаевых')),
                ('payment_method', models.CharField(max_length=35, verbose_name='Метод оплаты')),
            ],
            options={
                'verbose_name': 'Чек',
                'verbose_name_plural': 'Чеки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100, unique=True, verbose_name='Идентификатор')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('check_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.check', verbose_name='Чек')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт в чеке',
                'verbose_name_plural': 'Продукты в чеках',
            },
        ),
    ]
