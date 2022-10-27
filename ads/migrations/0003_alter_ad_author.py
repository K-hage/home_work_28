# Generated by Django 4.1.2 on 2022-10-26 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_location_lat_alter_location_lng'),
        ('ads', '0002_remove_ad_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='users.user', verbose_name='Автор'),
        ),
    ]
