# Generated by Django 4.1.7 on 2023-03-23 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_timemodel_asr_alter_timemodel_bomdod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionmodel',
            name='solat_times',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.timemodel'),
        ),
    ]
