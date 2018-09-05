# Generated by Django 2.1 on 2018-09-05 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='country',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='obj.Country', verbose_name='Country of competition'),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.IntegerField(null=True, verbose_name='Height of player in cm'),
        ),
        migrations.AlterField(
            model_name='player',
            name='jersey_number',
            field=models.IntegerField(null=True, verbose_name='Jersey number of player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=20, null=True, verbose_name='Position of player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.IntegerField(null=True, verbose_name='Weight of player in kg'),
        ),
    ]
