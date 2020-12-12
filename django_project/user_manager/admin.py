from django.contrib import admin
from .models import User, Product, Purchase  # Referral


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ["user_id", "name", "username"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	class Meta:
		fields = "__all__"


# @admin.register(Referral)
# class ReferralAdmin(admin.ModelAdmin):
# 	list_display = ("id", "referrer_id")


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
	list_display = ["id", "buyer", "product_id", "quantity", "amount", "shipping_address", "payed"]

# Register your models here.
