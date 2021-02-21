# Generated by Django 3.1.7 on 2021-02-20 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("materials", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="CuttingData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fz_base",
                    models.FloatField(
                        help_text="fz at ae=0.5d and ap=1d", verbose_name="fz (base)"
                    ),
                ),
                (
                    "vc_base",
                    models.FloatField(
                        help_text="vc at ae=0.5d and ap=1d", verbose_name="vc (base)"
                    ),
                ),
                (
                    "fz_factor_slotting",
                    models.FloatField(
                        default=1.0,
                        help_text="fz factor for slotting operations",
                        verbose_name="fz factor slotting",
                    ),
                ),
                (
                    "vc_factor_slotting",
                    models.FloatField(
                        default=1.0,
                        help_text="vc factor for slotting operations",
                        verbose_name="vc factor slotting",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.material",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cutting Data",
                "verbose_name_plural": "Cutting Data",
                "ordering": ("material", "tool"),
            },
        ),
        migrations.CreateModel(
            name="Machine",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "spindle_net_power_kw",
                    models.FloatField(verbose_name="Spindle net power (kW)"),
                ),
                (
                    "max_rpm",
                    models.PositiveIntegerField(verbose_name="Max spindle RPM (1/min)"),
                ),
                (
                    "max_vf",
                    models.FloatField(verbose_name="Max cutting speed (mm/min)"),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Tool Vendor",
                "verbose_name_plural": "Tool Vendors",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Tool",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("flute_count", models.PositiveIntegerField()),
                ("flute_length", models.FloatField(verbose_name="Flute length (mm)")),
                ("diameter", models.FloatField(verbose_name="Diameter (mm)")),
                (
                    "cutting_edge_angle",
                    models.FloatField(
                        default=90, verbose_name="Cutting edge angle KAPR (degree)"
                    ),
                ),
                (
                    "material",
                    models.CharField(
                        choices=[("HSS", "HSS"), ("CARBIDE", "Carbide")],
                        default="CARBIDE",
                        max_length=10,
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tools",
                        to="milling.vendor",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="CuttingRecipe",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "machine_max_rpm_override",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Max spindle RPM override"
                    ),
                ),
                (
                    "machine_max_vf_override",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Max cutting speed override"
                    ),
                ),
                (
                    "tool_fz_override",
                    models.FloatField(
                        blank=True, null=True, verbose_name="fz override"
                    ),
                ),
                (
                    "tool_vc_override",
                    models.FloatField(
                        blank=True, null=True, verbose_name="vc override"
                    ),
                ),
                (
                    "ae",
                    models.FloatField(blank=True, null=True, verbose_name="ae (mm)"),
                ),
                (
                    "ap",
                    models.FloatField(blank=True, null=True, verbose_name="ap (mm)"),
                ),
                (
                    "phi_selection",
                    models.CharField(
                        blank=True,
                        choices=[("C", "Center"), ("OC", "Off Center")],
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "cutting_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="milling.cuttingdata",
                    ),
                ),
                (
                    "machine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="milling.machine",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cutting Recipe",
                "verbose_name_plural": "Cutting Recipies",
            },
        ),
        migrations.AddField(
            model_name="cuttingdata",
            name="tool",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="milling.tool"
            ),
        ),
    ]