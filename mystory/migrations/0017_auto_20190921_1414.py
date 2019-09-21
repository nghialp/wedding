# Generated by Django 2.1 on 2019-09-21 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mystory', '0016_auto_20190921_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='blessing',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wedding_invitation',
            name='time_calendar',
            field=models.DateTimeField(verbose_name='Ngày Dương Lịch'),
        ),
        migrations.AlterField(
            model_name='wedding_invitation',
            name='time_lunar',
            field=models.DateTimeField(verbose_name='Ngày Âm Lịch'),
        ),
    ]
