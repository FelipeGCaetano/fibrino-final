# Generated by Django 4.1.4 on 2022-12-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FibrinoDev', '0010_rename_header_comandos_comando'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roteador',
            name='marca',
            field=models.CharField(choices=[('Huawei', 'Huawei'), ('TP-link', 'TP-link'), ('Intelbras', 'Intelbras'), ('Mercusys', 'Mercusys')], max_length=100),
        ),
    ]