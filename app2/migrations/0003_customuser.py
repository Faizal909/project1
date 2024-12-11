# Generated by Django 5.1.2 on 2024-11-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_table_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
