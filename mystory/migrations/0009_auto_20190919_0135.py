# Generated by Django 2.1 on 2019-09-18 18:35

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('mystory', '0008_auto_20190919_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blessing',
            name='blessing',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Lời chúc'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='decription',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Nội dung'),
        ),
        migrations.AlterField(
            model_name='image',
            name='decription',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Ghi chú'),
        ),
        migrations.AlterField(
            model_name='story',
            name='content',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Nội dung'),
        ),
    ]
