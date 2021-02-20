# Generated by Django 3.1.7 on 2021-02-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('flute_count', models.PositiveIntegerField()),
                ('flute_length', models.FloatField(verbose_name='Flute length (mm)')),
                ('diameter', models.FloatField(verbose_name='Diameter (mm)')),
                ('tip_angle', models.FloatField(verbose_name='Tip angle')),
                ('material', models.CharField(choices=[('HSS', 'HSS'), ('CARBIDE', 'Carbide')], default='CARBIDE', max_length=10)),
                ('drill_type', models.CharField(choices=[('SPOT_DRILL', 'Spiral Drill'), ('SPOT_DRILL', 'Spot Drill')], default='SPOT_DRILL', max_length=20)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]