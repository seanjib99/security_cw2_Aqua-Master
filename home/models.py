from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField
from registration.models import Customer
from math import floor
# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.CharField(max_length=100)
    marked_price = models.FloatField()
    selling_price = models.FloatField()
    available_quantity = models.PositiveIntegerField(default=0) #Remove this default option in the final project
    photo = models.ImageField(upload_to='products/')
    #Char Field For image alt #####-------Needed to be added--------#####
    return_policy = models.CharField(max_length=255)
    slug = models.SlugField()
    tags = models.CharField(max_length=300, default='')
    modified_date = models.DateField(auto_now=True)
    users_wishlist = models.ManyToManyField(User, blank=True, related_name='user_wishlist')

    def __str__(self):
        return self.name + '......'+self.weight

    @property
    def discount_percent(self):
        discount = (self.marked_price - self.selling_price)/self.marked_price
        return str(floor(discount * 100))

class MyCart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def sub_total(self):
        return str(self.quantity * self.product.selling_price)

STATUS_CHOICES = (
    ('pending', 'pending'),
    ('received', 'received'),
    ('packed', 'packed'),
    ('on_the_way', 'on_the_way'),
    ('delivered', 'delivered'),
    ('cancel', 'cancel'),
)

class OrderPlaced(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveBigIntegerField(default=0)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    ##--------------For Payment Integration--------------##
    #Payment_Method_Choices_Char_Field
    #Payment_Completed_Boolean_Field

    def __str__(self):
        return str(self.user.username + '      ' + self.customer.full_name + '     ' + self.product.name)

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message[0:15] + '...' + '    By   ' + self.full_name)

class SubscriptionEmail(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + '.....' + self.email
        