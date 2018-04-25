# Generated by Django 2.0.2 on 2018-04-24 16:29

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'permissions': (('view_invoice', 'Can view invoice'), ('pay_invoice', 'Can pay invoice'))},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sender_wallet_type',
            field=models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(django.db.models.query_utils.Q(('app_label', 'wallets'), ('model', 'btc'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'wallets'), ('model', 'ltc'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'wallets'), ('model', 'dash'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'wallets'), ('model', 'doge'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'wallets'), ('model', 'bcy'), _connector='AND'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='sended_invoices', to='contenttypes.ContentType'),
        ),
    ]