# Generated by Django 3.2.3 on 2021-09-10 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0010_myfood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myfood',
            name='dinner',
        ),
        migrations.RemoveField(
            model_name='myfood',
            name='lunch',
        ),
        migrations.CreateModel(
            name='Mylunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunch', models.CharField(max_length=40)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Mydinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner', models.CharField(max_length=40)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.login')),
            ],
        ),
    ]