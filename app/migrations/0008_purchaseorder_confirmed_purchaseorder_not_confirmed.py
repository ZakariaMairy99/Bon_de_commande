# Generated by Django 4.2.1 on 2023-09-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_purchaseorder_type_de_cable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='not_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]