# Generated by Django 3.0.5 on 2020-07-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20200720_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientSymptomsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom_name', models.CharField(max_length=255)),
            ],
        ),
    ]
