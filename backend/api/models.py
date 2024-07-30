from django.db import models

class Store(models.Model):
    store_number = models.IntegerField()
    store_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    store_location = models.CharField(max_length=255, null=True, blank=True)
    county_number = models.IntegerField()
    county = models.CharField(max_length=100)
    
    def __str__(self):
        return self.store_name

class Item(models.Model):
    item_number = models.IntegerField()
    item_desc = models.CharField(max_length=255)
    pack = models.IntegerField()
    bottle_volume_ml = models.IntegerField()
    state_bottle_cost = models.DecimalField(max_digits=10, decimal_places=2)
    state_bottle_retail = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.item_desc

class Vendor(models.Model):
    vendor_number = models.IntegerField()
    vendor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.vendor_name

class Category(models.Model):
    category_number = models.IntegerField()
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Sale(models.Model):
    invoice_item_number = models.CharField(max_length=255)
    date = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bottles_sold = models.IntegerField()
    sale_dollars = models.DecimalField(max_digits=10, decimal_places=2)
    volume_sold_liters = models.DecimalField(max_digits=10, decimal_places=2)
    volume_sold_gallons = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.invoice_item_number} - {self.date}"