# Generated by Django 4.1.4 on 2022-12-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FibrinoDev', '0013_remove_roteadorlogin_roteador_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roteador',
            name='foto',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
