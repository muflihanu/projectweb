# Generated by Django 5.1.6 on 2025-02-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packagecreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=700)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usersign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendorregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('businessname', models.CharField(max_length=30)),
                ('businnesregistornumber', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
