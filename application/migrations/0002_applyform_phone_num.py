# Generated by Django 4.0 on 2023-08-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyform',
            name='phone_num',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
