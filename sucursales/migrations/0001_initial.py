# Generated by Django 4.2.7 on 2023-12-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('country', models.TextField()),
                ('region', models.TextField()),
                ('city', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
