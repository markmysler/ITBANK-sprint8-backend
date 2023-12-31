# Generated by Django 4.2.7 on 2023-12-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(choices=[('HIPOTECARIO', 'HIPOTECARIO'), ('PERSONAL', 'PERSONAL'), ('PRENDARIO', 'PRENDARIO')], default='PERSONAL', max_length=20)),
                ('loan_date', models.DateField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('target_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.cuenta')),
            ],
        ),
    ]
