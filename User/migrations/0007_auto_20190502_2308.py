# Generated by Django 2.2 on 2019-05-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20190502_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_last_access',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
