# Generated by Django 4.1.4 on 2022-12-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FibrinoDev', '0014_alter_roteador_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roteador',
            name='foto',
            field=models.ImageField(blank=True, max_length=255, upload_to=''),
        ),
    ]