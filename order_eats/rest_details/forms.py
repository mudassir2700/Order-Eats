from django import forms
from .models  import restaurant_details,setting
from menu.models import menu

class Rest_Info(forms.ModelForm):
	class Meta:
		model=restaurant_details
		fields=['Restaurant_name','Area','City','zipcode','rest_choice','short_description','address','web_url','cuisine_type','profile_image','logo_image','location_image','Weekday_timings','Weekend_timings','cost_for_two_people','buffet','buffet_timing','alcohol_served','Cuisines_You_Offer','Type_of_dining','Restaurant_Special_Items']


class res_info(forms.ModelForm):
	class Meta:
		model=setting
		fields=['minimum_party_size','maximum_party_size','no_of_reservations_per_hour','breakfast_hours','lunch_hours','dinner_hours']

class menu_info(forms.ModelForm):
	class Meta:
		model=menu
		fields=['item','price','vegetarian_meal','menu_type']

class menu_infoadd(forms.ModelForm):
	class Meta:
		model=menu
		fields=['menu_id','item','price','vegetarian_meal','drinks','menu_type']