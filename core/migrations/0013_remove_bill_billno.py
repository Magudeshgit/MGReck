# Generated by Django 5.0.4 on 2024-04-26 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_bill_billdate_bill_billstatus_bill_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='billno',
        ),
    ]
