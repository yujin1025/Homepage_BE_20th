# Generated by Django 4.2.2 on 2023-07-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('birthdate', models.DateField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('남성', '남성'), ('여성', '여성')], max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('first_preference', models.CharField(choices=[('보컬', '보컬'), ('드럼', '드럼'), ('기타', '기타'), ('베이스', '베이스'), ('신디', '신디')], max_length=20)),
                ('second_preference', models.CharField(choices=[('보컬', '보컬'), ('드럼', '드럼'), ('기타', '기타'), ('베이스', '베이스'), ('신디', '신디')], max_length=20)),
                ('play_instrument', models.CharField(blank=True, max_length=200)),
                ('motive', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
