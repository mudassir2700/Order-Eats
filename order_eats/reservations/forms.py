from django import forms
from .models  import Appointment

class app(forms.ModelForm):
	class Meta:
		model=Appointment
		fields=['date','cust_email','contact_no','name','tablesize','mealchoice','slot']
