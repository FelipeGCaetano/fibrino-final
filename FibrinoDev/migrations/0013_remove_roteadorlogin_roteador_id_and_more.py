# Generated by Django 4.1.4 on 2022-12-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FibrinoDev', '0012_alter_roteadorlogin_roteador_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roteadorlogin',
            name='roteador_id',
        ),
        migrations.AddField(
            model_name='roteadorlogin',
            name='marca_roteador',
            field=models.CharField(choices=[('Huawei', 'Huawei'), ('TP-link', 'TP-link'), ('Intelbras', 'Intelbras'), ('Mercusys', 'Mercusys'), ('D-link', 'D-link'), ('Tenda', 'Tenda')], default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='roteador',
            name='marca',
            field=models.CharField(choices=[('Huawei', 'Huawei'), ('TP-link', 'TP-link'), ('Intelbras', 'Intelbras'), ('Mercusys', 'Mercusys'), ('D-link', 'D-link'), ('Tenda', 'Tenda')], max_length=100),
        ),
    ]