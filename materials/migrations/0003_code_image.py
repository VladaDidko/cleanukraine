# Generated by Django 2.2 on 2019-04-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_remove_code_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='material_pics'),
        ),
    ]