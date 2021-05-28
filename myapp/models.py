from django.db import models

class Customer(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Pincode = models.IntegerField(max_length=100)

class Product(models.Model):
    Product_name = models.CharField(max_length=100)
    Unit_price = models.IntegerField()

class Order(models.Model):
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Productsss = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    Unit_price = models.IntegerField()
    Quntity = models.IntegerField()
    Total_price = models.IntegerField()
    Created_date = models.DateTimeField(auto_now_add=True)

    
