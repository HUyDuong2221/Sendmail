# Generated by Django 4.0.5 on 2022-10-19 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_gmail', '0003_alter_send_mail_send_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='read_mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('send_date', models.DateTimeField()),
                ('From', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='send_mail',
            name='send_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 19, 15, 19, 22, 130702)),
        ),
    ]
