# Generated by Django 3.1 on 2020-08-29 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_choice', '0003_auto_20200829_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200),
        ),
    ]