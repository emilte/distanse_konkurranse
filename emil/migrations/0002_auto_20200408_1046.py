# Generated by Django 3.0.5 on 2020-04-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Kommentar'),
        ),
    ]