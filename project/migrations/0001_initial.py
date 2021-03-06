# Generated by Django 2.1.4 on 2018-12-04 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('date_project', models.DateField()),
                ('date_upload', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('video', models.FileField(null=True, upload_to='')),
                ('texte', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'projet',
                'ordering': ['date_upload'],
            },
        ),
    ]
