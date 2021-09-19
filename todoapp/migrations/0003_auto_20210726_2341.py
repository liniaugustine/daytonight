# Generated by Django 3.2.3 on 2021-07-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newtask', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='userdetails',
            name='phone',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
