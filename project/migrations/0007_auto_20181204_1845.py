# Generated by Django 2.1.4 on 2018-12-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20181204_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'projet'},
        ),
        migrations.AlterField(
            model_name='project',
            name='view_order',
            field=models.IntegerField(blank=True, choices=[(1, 'top left'), (2, 'top right'), (3, 'bottom left'), (4, 'bottom right')], null=True),
        ),
    ]
