# Generated by Django 4.1.2 on 2022-11-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhut_app', '0005_adddetailsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddetailsmodel',
            name='rimage',
            field=models.FileField(upload_to='static'),
        ),
    ]
