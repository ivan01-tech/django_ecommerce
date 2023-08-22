# Generated by Django 2.2.13 on 2023-08-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SH', 'SHIRT'), ('SW', 'Sport Wear'), ('OW', 'Outwear'), ('TO', 'Tools')], default='SH', max_length=40),
        ),
    ]
