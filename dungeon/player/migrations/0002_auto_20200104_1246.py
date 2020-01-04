# Generated by Django 2.2.7 on 2020-01-04 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dungeonroom', '0004_auto_20200104_1024'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dungeonroom.Room'),
            preserve_default=False,
        ),
    ]
