# Generated by Django 3.1.7 on 2021-02-26 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("milling", "0004_tooltable"),
    ]

    operations = [
        migrations.RenameModel(old_name="ToolTable", new_name="ToolTableEntry")
    ]
