# Generated by Django 3.0.5 on 2020-05-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=75)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
