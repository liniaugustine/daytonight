# Generated by Django 3.2.3 on 2021-09-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_auto_20210901_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='mycolor',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
