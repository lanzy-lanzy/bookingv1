# Generated by Django 5.1.6 on 2025-03-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('gcash', 'GCash')], default='cash', max_length=50),
        ),
    ]
