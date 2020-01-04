# Generated by Django 2.2.7 on 2020-01-04 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dungeonroom', '0004_auto_20200104_1024'),
        ('player', '0003_item_quality_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='experience',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_level',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('monster_type', models.CharField(max_length=200)),
                ('armor_class', models.PositiveIntegerField(default=0)),
                ('health_points', models.IntegerField(default=0)),
                ('experience_value', models.PositiveIntegerField(default=0)),
                ('damage', models.PositiveIntegerField(default=0)),
                ('mana_points', models.PositiveIntegerField(default=0)),
                ('mana_regen', models.PositiveIntegerField(default=0)),
                ('mage', models.BooleanField(default=False)),
                ('healer', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dungeonroom.Room')),
            ],
        ),
    ]
