# Generated by Django 4.1.3 on 2022-12-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNew', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultimo_paseo', models.DateField()),
                ('realizado', models.BooleanField()),
                ('nombre_del_paseo', models.CharField(max_length=100)),
            ],
        ),
    ]