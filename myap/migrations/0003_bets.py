# Generated by Django 3.2.16 on 2023-01-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myap', '0002_todaylines'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=3)),
                ('line', models.IntegerField(default=0)),
            ],
        ),
    ]
