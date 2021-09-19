# Generated by Django 3.2.3 on 2021-09-07 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_notes_mycolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myfood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning', models.CharField(max_length=40)),
                ('lunch', models.CharField(max_length=40)),
                ('dinner', models.CharField(max_length=40)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.login')),
            ],
        ),
    ]
