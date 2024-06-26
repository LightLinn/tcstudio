# Generated by Django 3.2.16 on 2022-11-17 08:09

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentList',
            fields=[
                ('ContentId', models.AutoField(primary_key=True, serialize=False)),
                ('BlockName', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=150)),
                ('Content', ckeditor.fields.RichTextField()),
                ('ImgPath', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('Alt', models.CharField(max_length=20)),
                ('CreateDate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
