# Generated by Django 3.0.5 on 2020-07-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_extendeduser_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='aboutMe',
            field=models.CharField(max_length=200),
        ),
    ]
