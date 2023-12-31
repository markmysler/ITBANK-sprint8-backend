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
            name='Tarjeta',
            fields=[
                ('card_number', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('cvv', models.IntegerField(blank=True, db_column='CVV', null=True)),
                ('emision_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('card_type', models.CharField(choices=[('CREDITO', 'CREDITO'), ('DEBITO', 'DEBITO')], default='DEBITO', max_length=25)),
                ('card_issuer', models.CharField(choices=[('VISA', 'VISA'), ('MASTER_CARD', 'MASTER_CARD'), ('AMERICAN_EXPRESS', 'AMERICAN_EXPRESS')], default='VISA', max_length=25)),
                ('customer_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('related_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.cuenta')),
            ],
        ),
    ]
