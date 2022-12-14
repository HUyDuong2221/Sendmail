# Generated by Django 4.0.5 on 2022-10-25 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_gmail', '0005_alter_read_mail_send_date_alter_send_mail_send_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='send_mail',
            name='send_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 25, 13, 24, 17, 68406)),
        ),
    ]
