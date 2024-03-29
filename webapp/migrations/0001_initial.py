# Generated by Django 4.1.6 on 2023-03-06 15:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import webapp.models.tasks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Слишком коротко!'), webapp.models.tasks.CustomDescriptionValidator()], verbose_name='Описание')),
                ('detailed_description', models.TextField(blank=True, max_length=2000, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Слишком коротко!'), webapp.models.tasks.CustomDetailedValidator()], verbose_name='Детально')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время и дата обновления')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Время и дата удаления')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.status')),
                ('type', models.ManyToManyField(to='webapp.type')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задание',
            },
        ),
    ]
