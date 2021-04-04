# Generated by Django 3.1.4 on 2021-04-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meat', models.CharField(max_length=100)),
                ('side1', models.CharField(max_length=100)),
                ('side2', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
