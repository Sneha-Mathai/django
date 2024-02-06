# Generated by Django 4.2.2 on 2024-02-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=50)),
                ('pic', models.ImageField(null=True, upload_to='uploadimage')),
            ],
        ),
    ]
