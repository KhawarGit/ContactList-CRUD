# Generated by Django 4.2.4 on 2024-02-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=200)),
                ('last_Name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('comment', models.TextField()),
            ],
        ),
    ]
