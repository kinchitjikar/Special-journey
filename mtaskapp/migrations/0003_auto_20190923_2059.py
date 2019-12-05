# Generated by Django 2.2.5 on 2019-09-23 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mtaskapp', '0002_auto_20190909_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='current_status',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='current_task',
            new_name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
