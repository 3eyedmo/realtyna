# Generated by Django 3.2.18 on 2023-05-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_delete_reservationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='name',
            field=models.CharField(max_length=1023),
        ),
    ]
