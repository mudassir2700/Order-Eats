from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from multiselectfield import MultiSelectField
from django.utils.text import slugify
# Create your models here.
class restaurant_details(models.Model):
	ITALIAN='ITALIAN'
	MEXICAN='MEXICAN'
	CHINESE='CHINESE'
	MUGHLAI='MUGHLAI'
	MULTICUISINE='MULTICUISINE'
	cuisine_choices=(
	(ITALIAN,'ITALIAN'),
	(MEXICAN,'MEXICAN'),
	(CHINESE,'CHINESE'),
	(MUGHLAI,'MUGHLAI'),
	(MULTICUISINE,'MULTICUISINE'),
	)

	
	in_process='In Process'
	accepted='accepted'
	status_choice=(
		(in_process,'In Process'),
		(accepted,'accepted'),
		)

	dineout ='Dine-Out Restaurants'
	pub='Pubs and Bars'
	cafe='Cafes'
	desserts='Desserts'
	rest_choice=(
		(dineout,'Dine-Out Restaurants'),
		(pub,'Pubs and Bars'),
		(cafe,'Cafes'),
		(desserts,'Desserts'),
		)

	ITALIAN='ITALIAN'
	MEXICAN='MEXICAN'
	CHINESE='CHINESE'
	MUGHLAI='MUGHLAI'
	north = 'North Indian'
	south = 'South Indian'
	rolls = 'Rolls'
	kebabs = 'Kebabs'
	momos = 'Momos'
	fastfood = 'Fast Food'
	dessert = 'Dessert'
	icecream = 'Ice-Cream'
	cui_choices=(
	(ITALIAN,'Italian'),
	(MEXICAN,'Mexican'),
	(CHINESE,'Chinese'),
	(MUGHLAI,'Mughlai'),
	(north,'North Indian'),
	(south,'South Indian'),
	(rolls,'Rolls'),
	(kebabs,'Kebabs'),
	(momos,'Momos'),
	(fastfood,'Fast Food'),
	(dessert,'Dessert'),
	(icecream,'Ice-Cream'),
	)

	casual_dining='Casual Dining'
	fine_dining = 'Fine Dining'
	bar = 'Bar'
	cafe = 'Cafe'
	food_court = 'Food court'
	quick_bytes = 'Quick Bytes'
	bakeries = 'Bakeries'

	dine_type=(

		(casual_dining,'Casual Dining'),
		(fine_dining,'Fine Dining'),
		(bar,'Bar'),
		(cafe,'Cafe'),
		(food_court,'Food Court'),
		(quick_bytes,'Quick Bytes'),
		(bakeries,'Bakeries'),
		)  




	Restaurant_name=models.CharField(max_length=20,blank=False)
	Area=models.CharField(max_length=20,blank=False)
	City=models.CharField(max_length=50,blank=True)
	status=models.CharField(max_length=20,blank=False,choices=status_choice,default='In Process')
	cuisine_type=models.CharField(max_length=30,choices=cuisine_choices,blank=True)
	rest_choice=models.CharField(max_length=50,blank=True,choices=rest_choice)
	zipcode=models.PositiveIntegerField(max_length=20,blank=False)
	created=models.DateTimeField(auto_now_add=True)
	slug=models.SlugField(blank=True)
	owner=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='owners')
	web_url=models.CharField(max_length=100,blank=False)
	gmap_url=models.CharField(max_length=100,blank=False,default='DEFAULT VALUE')
	short_description=models.CharField(max_length=200,blank=False,default='DEFAULT VALUE')
	profile_image=models.ImageField(upload_to='profile_image/',blank=True)
	logo_image=models.ImageField(upload_to='profile_image',blank=True)
	location_image=models.ImageField(upload_to='profile_image',blank=True)
	address=models.CharField(max_length=200,blank=True)
	buffet=models.BooleanField(default=False)
	buffet_timing=models.TimeField(blank=True,null=True)
	alcohol_served=models.BooleanField(default=False)
	Pure_vegetarian=models.BooleanField(default=False)
	cost_for_two_people = models.PositiveIntegerField(blank=True,null=True)
	Cuisines_You_Offer=MultiSelectField(choices=cui_choices,blank=True,null=True)
	Type_of_dining = MultiSelectField(choices=dine_type,blank=True,null=True)
	Restaurant_Special_Items=models.CharField(max_length=300,blank=True)
	Weekday_timings=models.CharField(max_length=50,blank=True)
	Weekend_timings=models.CharField(max_length=50,blank=True)
	
	def __str__(self):
		return self.cuisine_type

	def __str__(self):
		return self.location

	def __str__(self):
		return self.short_description

	def __str__(self):
		return self.web_url

	def __str__(self):
		return self.Restaurant_name

def create_slug(instance,new_slug=None):
	slug=slugify(instance.Restaurant_name)
	if new_slug is not None:
		slug=new_slug
	queryset=restaurant_details.objects.filter(slug=slug).order_by('id')
	exists=queryset.exists()
	if exists:
		new_slug='%s-%s' %(slug,queryset.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug


def pre_save_restdetails_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

pre_save.connect(pre_save_restdetails_receiver,sender=restaurant_details)


class setting(models.Model):
	minimum_party_size=models.PositiveIntegerField(max_length=2,default=2,blank=True)
	maximum_party_size=models.PositiveIntegerField(max_length=10,default=10,blank=True)
	no_of_reservations_per_hour=models.PositiveIntegerField(max_length=10,default=10,blank=True)
	breakfast_hours=models.TimeField(blank=True,null=True)
	lunch_hours=models.TimeField(blank=True,null=True)
	dinner_hours=models.TimeField(blank=True,null=True)
	restaur_name = models.ForeignKey(restaurant_details,on_delete=models.SET_NULL,null=True,related_name='restaurant_name')
	restaur_slug =models.CharField(max_length=20,blank=False,default='Default Slug')
