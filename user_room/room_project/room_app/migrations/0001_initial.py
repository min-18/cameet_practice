# Generated by Django 4.1 on 2022-08-11 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('age', models.IntegerField(default=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_title', models.CharField(max_length=20)),
                ('room_interest', models.CharField(max_length=20)),
                ('room_place', models.CharField(max_length=50)),
                ('room_date', models.DateField(auto_now_add=True)),
                ('room_time', models.TimeField(auto_now_add=True)),
                ('room_headcount', models.IntegerField(default=1)),
                ('room_status', models.IntegerField(default=0)),
                ('room_created_time', models.DateTimeField(auto_now_add=True)),
                ('user_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='room_app.user')),
            ],
        ),
    ]