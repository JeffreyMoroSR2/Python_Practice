# Generated by Django 4.0 on 2021-12-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0005_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
    ]
