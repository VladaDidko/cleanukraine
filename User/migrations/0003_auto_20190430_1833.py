# Generated by Django 2.2 on 2019-04-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20190430_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Ч', 'Чоловік'), ('Ж', 'Жінка')], default='Ч', max_length=1),
        ),
    ]
