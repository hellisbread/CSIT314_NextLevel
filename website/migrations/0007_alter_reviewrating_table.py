# Generated by Django 4.1.2 on 2022-11-15 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_reviewrating_review'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='reviewrating',
            table='review_rating',
        ),
    ]
