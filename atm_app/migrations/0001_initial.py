# Generated by Django 5.1.4 on 2024-12-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("acc_no", models.IntegerField(unique=True)),
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField()),
                ("adhaar_no", models.IntegerField(max_length=12, unique=True)),
                ("mobile", models.IntegerField(max_length=10, unique=True)),
                ("balance", models.DecimalField(decimal_places=2, max_digits=10)),
                ("pin", models.IntegerField(max_length=4)),
            ],
        ),
    ]