# Generated by Django 5.1.3 on 2024-11-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='name',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
