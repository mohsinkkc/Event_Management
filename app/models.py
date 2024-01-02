from django.db import models
import datetime
# Create your models here.
class User(models.Model):
	user_type=models.CharField(max_length=100,default='admin')
	name=models.CharField(max_length=100)
	email=models.EmailField()
	number=models.IntegerField()
	password=models.CharField(max_length=200)
	gender=models.CharField(max_length=100)
	image=models.ImageField(upload_to='new_image/')


	def __str__(self):
		return self.name

class Service(models.Model):
	category=models.CharField(max_length=100)

	def __str__(self):
		return self.category


class Event(models.Model):
	service=models.ForeignKey(Service,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	sub_category=models.CharField(max_length=500,null=True)
	hall_name=models.CharField(max_length=200)
	location=models.CharField(max_length=300)
	price=models.IntegerField()
	desc=models.CharField(max_length=500)
	date=models.DateField(null=True)
	image=models.ImageField(upload_to="images/")

	def __str__(self):
		return self.service.category+' - '+ self.sub_category

class Rent(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	n_email=models.EmailField()
	number=models.IntegerField()
	company=models.CharField(max_length=200)
	venue_name=models.CharField(max_length=300)
	event_type=models.CharField(max_length=500)
	date_request=models.DateField()
	date_end=models.DateField()
	image=models.ImageField(upload_to="images/",null=True)
	desc=models.CharField(max_length=800)

	def __str__(self):
		return self.company+' - '+self.venue_name	

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
	event=models.ForeignKey(Event,on_delete=models.CASCADE)
	date=models.DateField(default=datetime.date.today,null=True)
	payment_status=models.BooleanField(default=False)

	def __str__(self):
		return self.event.sub_category

class Transaction(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	amount=models.IntegerField()
	razorpay_order_id=models.CharField(max_length=100,null=True,blank=True)
	razorpay_payment_id=models.CharField(max_length=100,null=True,blank=True)
	razorpay_payment_signature=models.CharField(max_length=100,null=True,blank=True)
	date=models.DateField(default=datetime.date.today,null=True)

	def __str__(self):
		return self.user.name