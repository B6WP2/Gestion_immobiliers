# Generated by Django 4.2.5 on 2023-09-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App_immobiliers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="photo_de_profil",
            field=models.ImageField(
                blank=True, null=True, upload_to="photos_de_profil/"
            ),
        ),
        migrations.AlterField(
            model_name="bienimmobilier",
            name="prix",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
