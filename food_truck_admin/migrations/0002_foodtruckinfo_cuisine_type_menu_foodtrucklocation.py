# Generated by Django 4.2.9 on 2024-01-11 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_truck_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtruckinfo',
            name='cuisine_type',
            field=models.CharField(default=19, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_gluten_free', models.BooleanField(default=False)),
                ('food_truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_truck_admin.foodtruckinfo')),
            ],
        ),
        migrations.CreateModel(
            name='FoodTruckLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('food_truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_truck_admin.foodtruckinfo')),
            ],
        ),
    ]
