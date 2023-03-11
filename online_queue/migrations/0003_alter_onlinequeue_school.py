# Generated by Django 4.1.7 on 2023-03-11 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_school_spots'),
        ('online_queue', '0002_alter_onlinequeue_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinequeue',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queue', to='school.school', verbose_name='школа'),
        ),
    ]
