# Generated by Django 5.2.1 on 2025-05-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_heroes_pseudonym_villain_pseudonym'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
    ]
