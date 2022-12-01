# Generated by Django 4.1.3 on 2022-12-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=16, unique=True)),
                ('social_volumes', models.FloatField(null=True)),
                ('social_contributes', models.FloatField(null=True)),
            ],
        ),
    ]
