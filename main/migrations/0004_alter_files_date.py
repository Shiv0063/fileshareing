# Generated by Django 4.2.3 on 2023-08-12 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_files_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 12, 15, 59, 15, 525040)),
        ),
    ]
