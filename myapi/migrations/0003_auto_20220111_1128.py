# Generated by Django 3.2.9 on 2022-01-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_rename_hero_disp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название мероприятия')),
                ('participants', models.CharField(max_length=200, verbose_name='Количество участников')),
                ('date', models.CharField(max_length=200, verbose_name='Дата')),
                ('place', models.CharField(max_length=200, verbose_name='Место')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
            ],
        ),
        migrations.DeleteModel(
            name='Disp',
        ),
    ]
