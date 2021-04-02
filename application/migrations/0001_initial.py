# Generated by Django 2.2.4 on 2021-04-01 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.TextField(default=0)),
                ('cost_to_make', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('price', models.CharField(max_length=10)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='favorites', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('products', models.ManyToManyField(related_name='ingredients', to='application.Product')),
                ('users', models.ManyToManyField(related_name='allergies', to='login.User')),
            ],
        ),
    ]
