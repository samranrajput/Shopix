# Generated by Django 5.1.3 on 2024-12-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category_name',
            field=models.CharField(max_length=100),
        ),
    ]
