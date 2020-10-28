# Generated by Django 3.1 on 2020-10-23 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='addSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homeapp.skill')),
            ],
        ),
    ]
