from django.contrib import admin

from .models import *

# Register your models here.

class showadmin_(admin.ModelAdmin):
    list_display = ["a_name","a_email","password"]
admin.site.register(ad,showadmin_)

class showdisplay(admin.ModelAdmin):
    list_display = ["u_name","u_email","u_password","u_phone","u_address","u_role","user_photo"]
admin.site.register(registermodel,showdisplay)

class showcategory(admin.ModelAdmin):
    list_display = ["cat_name"]
admin.site.register(category,showcategory)

class showproduct(admin.ModelAdmin):
    list_display = ["sellerid", "product_photo", "p_photo", "p_name", "cat_id", "price", "description", "in_stock"]
admin.site.register(product,showproduct)


class showadd_to_cart(admin.ModelAdmin):
    list_display = ["u_id","p_id","quantity","totalamount","orderstatus","orderid"]
admin.site.register(cart,showadd_to_cart)

class showwishlist(admin.ModelAdmin):
    list_display = ["p_id","u_id",]
admin.site.register(wishlist,showwishlist)

class showsubcription(admin.ModelAdmin):
    list_display = ["u_id","sub_type","sub_datetime"]
admin.site.register(subscription,showsubcription)

class showreview(admin.ModelAdmin):
    list_display = ["u_id","p_id","review_date","ratting","review"]
admin.site.register(review,showreview)

class showoder(admin.ModelAdmin):
    list_display = ('u_id','repeat_days','finaltotal','phone','address','paymode','timestamp','status','razorpay_order_id')
admin.site.register(ordermodel, showoder)

class showdelivery_partner(admin.ModelAdmin):
    list_display = ["delivery_name","delivery_mobile_no","od_id"]
admin.site.register(delivery_partner,showdelivery_partner)


class showcomplaint(admin.ModelAdmin):
    list_display = ["u_id","p_id","od_id","datetime","status","msg"]
admin.site.register(complaint,showcomplaint)

class showcontact(admin.ModelAdmin):
    list_display = ["name","email","subject","msg"]
admin.site.register(contact,showcontact)

