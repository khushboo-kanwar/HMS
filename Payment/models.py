from django.db import models # type: ignore

# Create your models here.
from users.models import User  # Assuming you have a custom User model

class Accounting(models.Model):
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)

    def __str__(self):
        return f"{self.name} ({self.type})"

class Invoice(models.Model):
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateField()
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.id} - {self.issued_to.username}"

class DobleEntry(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='entries')
    account = models.ForeignKey(Accounting, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_type = models.CharField(max_length=10, choices=[('debit', 'Debit'), ('credit', 'Credit')])
    date = models.DateField()

    def __str__(self):
        return f"{self.entry_type.capitalize()} - {self.amount} on {self.date}"
    
