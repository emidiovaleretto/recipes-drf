# Generated by Django 5.0.3 on 2024-05-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_ingredients_a_html',
            field=models.BooleanField(default=False),
        ),
    ]
