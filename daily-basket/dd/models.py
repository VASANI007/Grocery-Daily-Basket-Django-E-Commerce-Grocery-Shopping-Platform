from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
status = [('Yes', 'Yes'), ('No', 'No')]
status_1 = [('ordr confirm', 'order confirm'), ('order not confirm', 'order not confirm')]
status_2 = [('Success', 'Success'), ('Not Success', 'Not Success')]
comp = [('Received', 'Received'), ('Not Received', 'Not Received')]


class ad(models.Model):
    a_name = models.CharField(max_length=20)
    a_email = models.EmailField()
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.a_name


class registermodel(models.Model):
    u_name = models.CharField(max_length=30, null=True)
    u_email = models.EmailField(unique=True, blank=True, null=True)
    u_phone = models.BigIntegerField(unique=True, blank=True, null=True)
    u_password = models.CharField(max_length=8, null=True)
    u_address = models.TextField()
    u_role = models.CharField(max_length=10, null=True)
    u_image = models.ImageField(upload_to='Photos',null=True)

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.u_image.url))

    user_photo.allow_tags = True

    def __str__(self):
        return self.u_name


class category(models.Model):
    cat_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.cat_name


class product(models.Model):
    image = models.ImageField(upload_to='Photos', null=True)
    p_image = models.ImageField(upload_to='Photos', null=True)
    p_name = models.CharField(max_length=100, null=True)
    cat_id = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField(null=True)
    in_stock = models.CharField(max_length=10, choices=status, null=True)
    sellerid=models.ForeignKey(registermodel,on_delete=models.CASCADE)

    def product_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    product_photo.allow_tags = True

    def p_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.p_image.url))
    
    def __str__(self):
        return self.p_name


class cart(models.Model):
    u_id = models.ForeignKey(registermodel, on_delete=models.CASCADE)
    p_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalamount = models.FloatField()
    orderstatus = models.IntegerField()
    orderid = models.IntegerField()


class wishlist(models.Model):
    u_id = models.ForeignKey(registermodel, on_delete=models.CASCADE, null=True)
    p_id = models.ForeignKey(product, on_delete=models.CASCADE)


class subscription(models.Model):
    u_id = models.ForeignKey(registermodel, on_delete=models.CASCADE)
    sub_type = models.CharField(max_length=20)
    sub_datetime = models.DateTimeField()


class review(models.Model):
    u_id = models.ForeignKey(registermodel, on_delete=models.CASCADE)
    p_id = models.ForeignKey(product, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)
    ratting = models.IntegerField()
    review = models.TextField()
    image = models.ImageField(upload_to='Review_Photos', null=True, blank=True)


class ordermodel(models.Model):
    u_id = models.ForeignKey(registermodel, on_delete=models.CASCADE)
    c_id = models.ForeignKey(cart, on_delete=models.CASCADE, null=True)
    p_id = models.ForeignKey(product, on_delete=models.CASCADE,null=True)
    finaltotal = models.FloatField()
    repeat_days = models.CharField(max_length=100, null=True, blank=True)
    phone = models.BigIntegerField()
    address = models.TextField()
    paymode = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)


class delivery_partner(models.Model):
    delivery_name = models.CharField(max_length=20, null=True)
    delivery_mobile_no = models.BigIntegerField()
    od_id = models.ForeignKey(ordermodel, on_delete=models.CASCADE)

class complaint(models.Model):
    u_id = models.ForeignKey(registermodel, on_delete=models.CASCADE)
    p_id = models.ForeignKey(product, on_delete=models.CASCADE)
    od_id = models.ForeignKey(ordermodel, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=comp, null=True)
    msg = models.TextField()

class contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=30,null=True)
    msg=models.TextField(null=True)
