# Generated by Django 4.1.4 on 2022-12-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FibrinoDev', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIAuth',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]