# Generated by Django 3.2.4 on 2021-06-30 06:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescriptions',
            name='visit',
        ),
        migrations.AddField(
            model_name='patients',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='symptoms',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registry.symptoms'),
            preserve_default=False,
        ),
    ]
