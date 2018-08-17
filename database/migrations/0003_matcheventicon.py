# Generated by Django 2.1 on 2018-08-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_discordusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchEventIcon',
            fields=[
                ('event', models.IntegerField(primary_key=True, serialize=False, verbose_name='Event')),
                ('eventIcon', models.CharField(default='', max_length=50, verbose_name='Icon for the event')),
            ],
        ),
    ]