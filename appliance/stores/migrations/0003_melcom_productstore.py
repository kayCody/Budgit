# Generated by Django 4.1.2 on 2022-10-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_melcom_productdespription_alter_melcom_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='melcom',
            name='productStore',
            field=models.CharField(blank=True, choices=[('Melcom', 'Melcom'), ('CampuGhana', 'CampuGhana'), ('Franko', 'Franko Trading'), ('LG', 'LG'), ('Hisense', 'Hisense'), ('Samsung', 'Samsung'), ('Techno', 'Techno Ghana'), ('Goodluck', 'GoodLuck Africa')], max_length=120, null=True),
        ),
    ]
