# Generated by Django 4.1.2 on 2022-10-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='melcom',
            name='productDespription',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='melcom',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]