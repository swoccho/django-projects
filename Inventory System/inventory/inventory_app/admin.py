from django.contrib import admin
from . import models

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['product' , 'vendor' , 'quantity' ,'unit' ,'total_amount', 'purchase_date']
    search_fields = ['product__product' , 'vendor__vendor_name', 'product__unit__title' ]


class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name' , 'vendor_status']
    search_fields = ['vendor_name']


class UnitAdmin(admin.ModelAdmin):
    list_display = ['title' , 'short_name']
    search_fields = ['title' ]

class ProductAdmin(admin.ModelAdmin):
    list_display= ['product' , 'vendor' , 'price' ,'unit']
    search_fields = ['product' , 'vendor__vendor_name', 'unit__title' ]




class SaleAdmin(admin.ModelAdmin):
    list_display = ['product' ,'vendor' , 'quantity','unit','total_amount','sale_date']
    search_fields = ['product__product' , 'vendor__vendor_name', 'product__unit__title' ]


    

class InventoryAdmin(admin.ModelAdmin):
    search_fields = ['product__product' , 'vendor__vendor_name', 'product__unit__title' ]

    list_display = ['product' , 'vendor' , 'left_quantity', 'purchase_quantity' , 'sale_quantity' ,'product_unit' ,'purchase_date' , 'sale_date']

admin.site.register(models.Inventory, InventoryAdmin)

admin.site.register(models.Vendor , VendorAdmin)
admin.site.register(models.Units,UnitAdmin)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Sale,SaleAdmin)
admin.site.register(models.Purchase,PurchaseAdmin)