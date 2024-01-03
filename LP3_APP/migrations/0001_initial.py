# Generated by Django 4.2.9 on 2024-01-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idregion', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='region_images/')),
                ('cases', models.PositiveIntegerField()),
                ('deaths', models.PositiveIntegerField()),
                ('lethality', models.FloatField()),
            ],
        ),
    ]
