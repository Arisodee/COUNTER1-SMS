# Generated by Django 3.1.6 on 2021-02-23 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('username', models.CharField(default=None, max_length=10)),
                ('id_number', models.CharField(max_length=8, unique=True)),
                ('phone_number', models.CharField(default=None, max_length=13, unique=True)),
                ('email', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Talking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('api_key', models.CharField(blank=True, max_length=201, null=True)),
                ('recipients', models.TextField(blank=True, max_length=1000, null=True)),
                ('message', models.TextField(blank=True, max_length=200, null=True)),
                ('sender_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counter1app.profile')),
            ],
        ),
    ]
