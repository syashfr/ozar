# Generated by Django 3.1.1 on 2021-04-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designspace', '0005_auto_20210426_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='forked_from',
            field=models.IntegerField(blank=True, null=True, verbose_name='self'),
        ),
    ]
