# Generated by Django 4.0.6 on 2024-05-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaestroProducto',
            fields=[
                ('idp', models.IntegerField(primary_key=True, serialize=False)),
                ('nomprod', models.CharField(max_length=100)),
                ('descprod', models.CharField(max_length=300)),
                ('precio', models.IntegerField()),
                ('foto_prod', models.ImageField(blank=True, null=True, upload_to='fotos/')),
            ],
        ),
    ]