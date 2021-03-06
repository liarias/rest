# Generated by Django 2.1 on 2018-08-29 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServicioPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('pago', models.FloatField(null=True)),
                ('ciudad', models.CharField(max_length=75)),
                ('direccion', models.CharField(max_length=100)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to='api.Persona')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='api.Servicio')),
            ],
        ),
    ]
