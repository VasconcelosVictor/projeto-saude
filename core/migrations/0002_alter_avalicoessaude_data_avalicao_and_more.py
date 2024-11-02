# Generated by Django 5.1.2 on 2024-11-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avalicoessaude',
            name='data_avalicao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='avalicoessaude',
            name='diagnostico_preliminar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='avalicoessaude',
            name='observacoes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]