# Generated by Django 5.0.6 on 2024-06-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('address', models.TextField(null=True)),
                ('city', models.CharField(default='Unknown', max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('subject', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
    ]
