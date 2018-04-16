# Generated by Django 2.0.3 on 2018-04-16 19:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('canEdit', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('about', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=256)),
                ('canSee', models.BooleanField(default=True)),
                ('canRate', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_rating', models.PositiveIntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(10))),
                ('cumulated_rating', models.PositiveIntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(10))),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratings.User')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='ratings.User'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='ratings.User'),
        ),
    ]
