# Generated by Django 5.2.3 on 2025-07-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omega', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
