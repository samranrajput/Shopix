# Generated by Django 5.1.3 on 2024-12-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_banner_webname_delete_websetting_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebSetting',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False)),
                ('web_name', models.CharField(max_length=100)),
                ('banner_image', models.ImageField(upload_to='banner_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='WebName',
        ),
    ]
