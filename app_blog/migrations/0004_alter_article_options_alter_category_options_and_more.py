# Generated by Django 5.0.6 on 2024-06-05 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_category_options_alter_category_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Стаття', 'verbose_name_plural': 'Статті'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації', 'verbose_name_plural': 'Категорії для публікацій'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='app_blog.category', verbose_name='Категорія'),
        ),
    ]
