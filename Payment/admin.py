from django.contrib import admin # type: ignore
from .models import Accounting, Invoice, DobleEntry


@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'issued_to', 'total_amount', 'issued_date', 'due_date', 'is_paid')
    list_filter = ('is_paid', 'issued_date', 'due_date')
    search_fields = ('issued_to__username', 'id')


@admin.register(DobleEntry)
class DobleEntryAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'account', 'amount', 'entry_type', 'date')
    list_filter = ('entry_type', 'date', 'account')
    search_fields = ('invoice__id', 'account__name')
