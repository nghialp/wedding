# Generated by Django 2.2.5 on 2019-09-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystory', '0012_auto_20190919_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blessing',
            name='user',
        ),
        migrations.AddField(
            model_name='blessing',
            name='relation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mối quan hệ'),
        ),
        migrations.AlterField(
            model_name='blessing',
            name='blessing',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Lời chúc'),
        ),
    ]