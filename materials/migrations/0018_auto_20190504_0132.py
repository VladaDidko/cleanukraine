# Generated by Django 2.2 on 2019-05-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0017_auto_20190504_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='id',
        ),
        migrations.AddField(
            model_name='test',
            name='id_test',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
