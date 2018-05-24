from django.conf import settings

from celery.decorators import periodic_task
from datetime import timedelta
import blockcypher

from .models import Invoice
from .signals import invoice_is_paid


@periodic_task(run_every=timedelta(seconds=settings.CHECK_EVERY_SECONDS))
def check_transaction_confirmations():
    if settings.CHECK_TRANSACTION_CONFIRMATIONS:
        invoices = Invoice.objects.filter(is_paid=False, tx_ref__is_null=False)
        for invoice in invoices:
            details = blockcypher.get_transaction_details(
                tx_ref=invoice.tx_ref,
                coin_symbol=invoice.wallet.coin_symbol
            )
            if details['confirmations'] >= settings.DEFAULT_CONFIRMATIONS:
                invoice.is_paid = True
                invoice.save()
                invoice_is_paid.send(sender=Invoice, invoice_id=invoice.id)
