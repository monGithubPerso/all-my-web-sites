# Generated by Django 3.2.3 on 2021-06-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('number_person', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=255)),
                ('name_reservation', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
