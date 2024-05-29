# Generated by Django 3.2.16 on 2022-11-18 10:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20221117_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='Author',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bloglist',
            name='Catego',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bloglist',
            name='Content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bloglist',
            name='Desc',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bloglist',
            name='Tag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]