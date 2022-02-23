# Generated by Django 4.0.2 on 2022-02-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_builders', '0002_alter_form_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='form_builders.formgroup'),
        ),
    ]
