# Generated by Django 5.0.1 on 2024-03-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pc_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='image/')),
                ('proc', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('bat', models.CharField(max_length=255)),
                ('drive', models.CharField(max_length=255)),
                ('img1', models.ImageField(upload_to='image/')),
                ('img2', models.ImageField(upload_to='image/')),
                ('img3', models.ImageField(upload_to='image/')),
                ('comment', models.TextField(max_length=255)),
            ],
        ),
    ]
