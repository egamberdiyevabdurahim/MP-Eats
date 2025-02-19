# Generated by Django 5.1.3 on 2024-12-12 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_branch", "0003_branchproductsmodel"),
        ("app_company", "0003_restaurantproductsmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="branchproductsmodel",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="branch_products",
                to="app_company.restaurantproductsmodel",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="branchproductsmodel",
            unique_together={("branch", "restaurant")},
        ),
    ]
