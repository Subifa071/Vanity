# Generated by Django 4.0.6 on 2022-07-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_blog_formulation_blog_highlighted_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(blank=True, choices=[('skincare', 'Skin Care'), ('makeup', 'Makeup'), ('bath&body', 'Bath & Body')], default='skincare', max_length=100, null=True),
        ),
    ]
