# Generated by Django 4.2 on 2023-04-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=122)),
                ('weight', models.IntegerField()),
                ('hieght', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
    ]
