# Generated by Django 4.1.2 on 2022-10-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_melcom_productstore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='melcom',
            name='productDespription',
        ),
        migrations.RemoveField(
            model_name='melcom',
            name='productStore',
        ),
        migrations.RemoveField(
            model_name='melcom',
            name='productWebAddress',
        ),
        migrations.AlterField(
            model_name='melcom',
            name='productCat',
            field=models.CharField(max_length=120),
        ),
    ]
