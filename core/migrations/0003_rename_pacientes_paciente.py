# Generated by Django 5.1.2 on 2024-11-01 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_avalicoessaude_data_avalicao_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pacientes',
            new_name='Paciente',
        ),
    ]
