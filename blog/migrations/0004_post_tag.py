# Generated by Django 2.2.2 on 2019-06-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190608_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='ML', max_length=200),
        ),
    ]
