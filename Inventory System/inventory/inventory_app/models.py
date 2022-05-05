
from django.db import models
from django.utils import timezone



class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_mobile = models.CharField(max_length=15)
    vendor_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '1. Vendors'

    def __str__(self) :
        return self.vendor_name


class Units(models.Model):
    title = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name_plural = '2.Units'


class Product(models.Model):
    product = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = '3.Products'
    def __str__(self) :
        return self.product
     

class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(Units,on_delete=models.CASCADE , editable=False)
    total_amount = models.FloatField(editable=False)
    purchase_date = models.DateField(auto_now_add=timezone.now())


    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.product.price
        self.unit = self.product.unit

        super(Purchase,self).save(*args,**kwargs)

        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()

        if inventory:
            total_balance = inventory.left_quantity + self.quantity

        else:
            total_balance = self.quantity
        Inventory.objects.create(
            product = self.product,
            purchase = self,
            sale = None,
            vendor = self.vendor,
            left_quantity = total_balance,
            purchase_quantity = self.quantity,
            sale_quantity = None
        )

        

    def __str__(self) -> str:
        return self.product.product
    
    class Meta:
        verbose_name_plural = '4.Purchase'


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models. ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(Units, on_delete=models.CASCADE , editable=False)
    total_amount = models.FloatField(editable=False)
    sale_date = models.DateField(auto_now_add=timezone.now())


    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.product.price
        self.unit = self.product.unit
        super(Sale,self).save(*args,**kwargs)

        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()

        if inventory:
            total_balance = inventory.left_quantity - self.quantity

        Inventory.objects.create(
            product = self.product,
            purchase = None,
            sale = self,
            vendor = self.vendor,
            left_quantity = total_balance,
            purchase_quantity = None,
            sale_quantity = self.quantity
        )


    def __str__(self) -> str:
        return self.product.product


    class Meta:
        verbose_name_plural = '5.Sale'



class Inventory(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase,on_delete=models.CASCADE ,null=True)
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    purchase_quantity = models.FloatField(default=0 , null=True)
    sale_quantity = models.FloatField(default=0, null=True)
    left_quantity = models.FloatField()

    class Meta:
        verbose_name_plural = '6.Inventory'
        

    def __str__(self) -> str:
        return self.product.product

    
    def purchase_date(self):
        if self.purchase:
            return self.purchase.purchase_date

    def sale_date(self):
        if self.sale:
            return self.sale.sale_date

    def product_unit(self):
        return self.product.unit



