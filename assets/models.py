from django.db import models # type: ignore

# Create your models here.

class Asset(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    purchase_date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class AssetCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
    
class Proposal(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    proposal_date = models.DateTimeField(auto_now_add=True)
    proposed_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Proposal for {self.asset.name} - {self.status}"
    
class Rtainer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Invoice(models.Model):
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        invoice_date = models.DateTimeField(auto_now_add=True)
        due_date = models.DateTimeField()
        status = models.CharField(max_length=50, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')])
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"Invoice for {self.trainer.name} - {self.status}"    
        

class Purchase(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=200)
    warranty_period = models.IntegerField()  # in months
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Purchase of {self.asset.name} - {self.purchase_price}"
    
class CMMS(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    maintenance_date = models.DateTimeField(auto_now_add=True)
    maintenance_type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    service_provider = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Maintenance for {self.asset.name} - {self.maintenance_type}"
    
class School_and_Institute(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Music_Institute(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Childcare(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Driving_School(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Waste_Management(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Fix_Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class HubSpot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
