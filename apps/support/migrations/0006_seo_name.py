# Generated by Django 2.0.12 on 2019-08-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_auto_20190814_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
