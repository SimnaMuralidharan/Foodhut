# Generated by Django 4.1.2 on 2022-11-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhut_app', '0004_rename_nname_nonmodel_nitem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='adddetailsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rimage', models.FileField(upload_to='')),
                ('rid', models.IntegerField()),
                ('rname', models.CharField(max_length=25)),
                ('rno', models.IntegerField()),
                ('rloc', models.CharField(max_length=50)),
                ('ropen', models.TimeField()),
                ('rclose', models.TimeField()),
            ],
        ),
    ]
