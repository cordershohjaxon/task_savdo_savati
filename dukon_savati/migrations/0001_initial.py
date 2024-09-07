# Generated by Django 5.1.1 on 2024-09-07 12:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Katigoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('17943115-c888-4ed6-a916-12af4d906830'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('discription', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, max_length=50)),
                ('stock_products', models.IntegerField()),
                ('catigory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mahsulotlar', to='dukon_savati.katigoriya')),
            ],
        ),
    ]
