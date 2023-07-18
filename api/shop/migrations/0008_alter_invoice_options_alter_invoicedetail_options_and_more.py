# Generated by Django 4.2.3 on 2023-07-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_order_options_alter_orderdetail_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': 'Facture'},
        ),
        migrations.AlterModelOptions(
            name='invoicedetail',
            options={'verbose_name': 'Detail de Facture', 'verbose_name_plural': 'Details des Factures'},
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_details',
            field=models.FloatField(default=0, max_length=45),
        ),
    ]