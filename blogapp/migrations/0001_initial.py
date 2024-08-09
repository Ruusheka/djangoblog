# Generated by Django 5.0.8 on 2024-08-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=1200, null=True)),
                ('caption', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
