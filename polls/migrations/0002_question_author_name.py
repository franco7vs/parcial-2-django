# Generated by Django 5.1.3 on 2024-11-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
