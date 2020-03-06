from django.db import models
from rest_details.models import restaurant_details
from reservations.models import Appointment
from rest_details.models import restaurant_details
from django.db.models.signals import post_save,pre_save
# Create your models here.

class menu(models.Model):
	veg_starter='Vegetarian Starter'
	nonveg_starter='Nonveg Starter'
	veg_maincourse='Vegetarian maincourse'
	nonveg_maincourse='Nonveg maincourse'
	dessert='Dessert'
	Beverages='Beverages'
	roti='roti'
	veg_chinese='veg_chinese'
	nonveg_chinese='nonveg_chinese'
	wine='wine'
	beer='beer'
	vodka='vodka'
	redwine='redwine'
	pizza='pizza'
	burger='burger'

	menutype=(
		('veg_starter','Vegetarian Starter'),
		('nonveg_starter','Nonveg Starter'),
		('veg_maincourse','Vegetarian maincourse'),
		('nonveg_maincourse','Nonveg maincourse'),
		('dessert','Dessert'),
		('Beverages','Beverages'),
		('roti','Rotis'),
		('veg_chinese','veg_chinese'),
		('nonveg_chinese','nonveg_chinese'),
		('wine','wine'),
		('beer','beer'),
		('vodka','vodka'),
		('redwine','redwine'),
		('pizza','pizza'),
		('burger','burger')
		)

	rest_menu=models.ForeignKey(restaurant_details,on_delete=models.SET_NULL,null=True,related_name='menurestaurant')
	menu_id=models.CharField(max_length=500,blank=True)
	rest_menu_slug=models.CharField(max_length=200,blank=True)
	item=models.CharField(max_length=200,blank=False)
	price=models.DecimalField(blank=False,max_digits=6,decimal_places=2)
	vegetarian_meal=models.BooleanField(blank=True)
	drinks=models.BooleanField(blank=True,default=False)
	menu_type=models.CharField(blank=False,max_length=50,choices=menutype,default='Vegetarian maincourse')

	def __str__(self):
		return self.menu_id


def pre_save_slug(instance,sender,*args,**kwargs):
	ob=restaurant_details.objects.get(Restaurant_name=instance.rest_menu)
	if not instance.rest_menu_slug:
		instance.rest_menu_slug=ob.slug
pre_save.connect(pre_save_slug,sender=menu)


def pre_save_menuid(instance,sender,*args,**kwargs):
	x=instance.rest_menu_slug
	y=instance.menu_id
	res=x+y
	ob=menu.objects.all()
	for i in ob:
		if i.menu_id==res:
			res=res+y
	instance.menu_id=res

pre_save.connect(pre_save_menuid,sender=menu)


class cart(models.Model):
	rest_cart=models.ForeignKey(restaurant_details,on_delete=models.SET_NULL,null=True,related_name='cartrestaurant')
	item_name=models.CharField(max_length=200,blank=True)
	oid=models.CharField(max_length=100,blank=False)
	menu_id=models.CharField(max_length=500,blank=True)
	rest_menu_slug=models.CharField(max_length=200,blank=True)
	item=models.ForeignKey(menu,on_delete=models.SET_NULL,null=True,related_name='cartmenu')
	price=models.DecimalField(blank=False,max_digits=6,decimal_places=2)
	quantity=models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.oid

class checkout(models.Model):
	ord_id=models.CharField(max_length=100,blank=True)
	f_ord_id=models.ForeignKey(Appointment,on_delete=models.SET_NULL,null=True,related_name='checkoutrestaurant')
	cart_price=models.DecimalField(max_digits=10,decimal_places=4)
	tax=models.DecimalField(max_digits=4,decimal_places=2)
	total=models.DecimalField(max_digits=8,decimal_places=4)
	amount_paid=models.DecimalField(max_digits=8,decimal_places=4,default=0000.0000)
	amount_due=models.DecimalField(max_digits=8,decimal_places=4,default=0000.0000)
	payment=models.BooleanField(blank=False,default=False)

class review(models.Model):
	name=models.CharField(max_length=200,blank=False)
	review=models.TextField(blank=False)
	review_ordid=models.CharField(max_length=200,blank=True)
	review_slug=models.CharField(max_length=200,blank=True)

class chat(models.Model):
	name=models.CharField(max_length=200,blank=False)
	review=models.TextField(blank=False)
	review_ordid=models.CharField(max_length=200,blank=True)



