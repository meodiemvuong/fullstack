# Generated by Django 4.0.3 on 2022-04-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='product/')),
                ('description', models.TextField(max_length=2000)),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]