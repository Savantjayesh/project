# Generated by Django 4.2.5 on 2023-10-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('ck', 'Cakes'), ('pd', 'Papad'), ('pr', 'PuranPoli')], max_length=2)),
                ('Product_image', models.ImageField(upload_to='Product')),
            ],
        ),
        migrations.CreateModel(
            name='singup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('medal_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('contact', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
