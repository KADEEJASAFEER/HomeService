# Generated by Django 3.1 on 2020-10-23 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimatedamount', models.IntegerField()),
                ('location', models.CharField(max_length=120)),
                ('user', models.CharField(max_length=120)),
                ('workstatus', models.CharField(choices=[('notassigned', 'notassigned'), ('assigned', 'assigned'), ('completed', 'completed')], max_length=50)),
                ('workname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homeapp.skill')),
            ],
        ),
    ]
