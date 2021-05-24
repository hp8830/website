from django.contrib import admin
from .models import Product, Offers


class ProductAdmin(admin.ModelAdmin):
    list_display = ("productid", "productname", "price", "stock")


class OffersAdmin(admin.ModelAdmin):
    list_display = ("offerid", "offercode", "offerdescription", "offerdiscount")


admin.site.register(Product, ProductAdmin)
admin.site.register(Offers, OffersAdmin )
