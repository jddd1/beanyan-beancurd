from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name

class Feedback(models.Model):
	CATEGORY = (
			('Product Complaints', 'Product Complaints'),
			('Question', 'Question'),
			('Delivery Issues', 'Delivery Issues'),
			('Others', 'Others')
			) 
	customername = models.CharField(max_length=200,null=True)
	customeremail = models.CharField(max_length=200,null=True)
	customerphone = models.CharField(max_length=200,null=True)
	customeraddress = models.CharField(max_length=200,null=True)
	customerconcern = models.CharField(max_length=200, null=True, choices=CATEGORY)
	customermessage = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.customername

class Product(models.Model):
	CATEGORY = (
			('Tub', 'Tub'),
			('Cup', 'Cup'),
			('Soya Milk', 'Soya Milk'),
			('Add Ons', 'Add Ons')
			) 
	AVAIL = (
			('Available', 'Available'),
			('Out of Stock', 'Out of Stock'),
			)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	avail = models.CharField(max_length=200, null=True, choices=AVAIL)


	def __str__(self):
		return self.name

class Cart(models.Model):
	product_name = models.CharField(max_length=200, null=True)
	amount = models.FloatField(null=True)

	def __str__(self):
		return self.product_name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE) 
	cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
	message = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	
	def __int__(self):
		return self.id