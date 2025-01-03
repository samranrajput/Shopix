# Generated by Django 5.1.3 on 2024-12-30 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_websetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False)),
                ('banner_image', models.ImageField(upload_to='banner_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebName',
            fields=[
                ('web_name_id', models.AutoField(primary_key=True, serialize=False)),
                ('web_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='WebSetting',
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='web_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='administrator.webname'),
        ),
    ]
