# Generated by Django 4.1.2 on 2022-11-13 04:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_bidded_paper_table_alter_comment_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sent_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
