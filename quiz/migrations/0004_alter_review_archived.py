# Generated by Django 4.0.6 on 2022-08-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_review_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
