# Generated by Django 3.1.7 on 2021-02-26 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('milling', '0005_auto_20210226_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tooltableentry',
            options={'ordering': ('tool_number',), 'verbose_name': 'Tool Table Entry', 'verbose_name_plural': 'Tool Table Entries'},
        ),
    ]