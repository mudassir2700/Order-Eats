from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Count
import datetime
from .models import Appointment 
from rest_details.models import restaurant_details,setting
from django.http import HttpResponseRedirect
from django.urls import reverse
from.forms import app
from datetime import date, datetime,time,timedelta
from menu.models import menu,cart,checkout,review,chat
import decimal
# Create your views here.
def index(request,slug):
	ob=slug
	form=app(request.POST)
	if form.is_valid():
		form.save()
	return render(request, 'reservations/ad.html',{'ob':ob,'form':form})


def appoint(request):
#    if 'id' not in request.session:
#        return redirect ("/")
	appointments= Appointment.objects.all()
	last_app = Appointment.objects.last()
	o=review.objects.filter(review_slug=last_app.tablename_slug)
	subject = 'Unique Reference Number for table Booking'
	message =last_app.order_id +" "+"is your unique Reference Number for booking reservation in restaurant"+" "+last_app.tablename_restaur
	to_email = last_app.cust_email
	from_email = settings.EMAIL_HOST_USER
	to_list = [to_email,settings.EMAIL_HOST_USER]
	send_mail( subject, message, from_email,to_list,fail_silently=True)


	#appointments= Appointment.objects.filter(order_id=Appointment.order_id)
	#user= Appointment.objects.get(id=request.session['id'])
#    user= User.objects.get(id=request.session['id'])
	# others = User.objects.all().exclude(appoint__id=request.session['id'])
	context = {
		#{}"user": user,
		'time': date.today(),
		"appointments": appointments,
		'last_app':last_app,
		'o':o
	}
	return render(request, 'reservations/success.html', context)

def addi(request,slug):
	if request.method != "POST":
		messages.error(request,"Can't add like that!")
		return redirect('reservations:index')
	else:
		ob=restaurant_details.objects.get(slug=slug)
		ob1=setting.objects.get(restaur_slug=slug)
		print(ob.Restaurant_name)


		add_appoint=Appointment.objects.appointval(request.POST,ob,ob1)

		for i in add_appoint:
			print(i)
		if add_appoint[0] == False:
			for each in add_appoint[1]:
				messages.error(request, each) #for each error in the list, make a message for each one.
			#return redirect(reverse('reservations:addi'))
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		if add_appoint[0] == True:
			o=Appointment.objects.all()
			messages.success(request, 'Successfully Reserved')
			return redirect('reservations:appoint')

def cust_tablereserve_view(request):
	ob=Appointment.objects.all()
	q=request.POST.get("query")
	oid=q
	#ob1=restaurant_details.objects.all()
	for i in ob:
		if (((i.order_id==q) & (str(i.date) >= str(date.today()))) ) :
			rest_name=i.tablename_restaur

			rest=restaurant_details.objects.get(Restaurant_name=rest_name)
			obj=Appointment.objects.get(order_id=q)
			crt =cart.objects.filter(oid=q)
			check=checkout.objects.filter(ord_id=q)

			return render(request,'reservations/customer_tablereserve_check.html',{'obj':obj,'rest':rest,'crt':crt,'check':check,'oid':oid})
	messages.error(request,'Please enter your correct URF no (or) your appointment for URF no is in the past ')
	return redirect('account:homepage')


def cust_edit_reserve_view(request,oid):     
	instance=get_object_or_404(Appointment,order_id=oid)
	ob=Appointment.objects.get(order_id=oid)
	form=app(request.POST or None,instance=instance)
	if form.is_valid():
		error=[]
		instance=form.save(commit=False)
		date=form.cleaned_data['date']
		slot=form.cleaned_data['slot']
		restname=instance.tablename_restaur
		restslug=instance.tablename_slug
		ob1=setting.objects.get(restaur_slug=restslug)
		if(str(date)<str(date.today())):
			error.append('Please enter a future date')
		if len(Appointment.objects.filter(date = date ,slot=slot,tablename_restaur=restname)) >= ob1.no_of_reservations_per_hour:
			error.append("Oops!! Opted Time Slot is full, Please enter different Slot")
		if(str(slot)<str(datetime.now().strftime("%H:%M")) and str(date)<=str(date.today())):
			error.append('Please enter a future time slot')
		if len(error)>0:
			for each in error:
				messages.error(request,each)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		if(len(error)==0):
			instance.save()
			messages.success(request,'Congratulations.. your Resevation has been updated. Please Login again to verify')
			return redirect('account:homepage')
		#ob.date=form.cleaned_data['date']
		#print(form.cleaned_data['date'])
		#ob.cust_email=form.cleaned_data['cust_email']
		#ob.contact_no=form.cleaned_data['contact_no']
		#ob.task=form.cleaned_data['task']
		#ob.mealchoice=form.cleaned_data['mealchoice']
		#ob.tablesize=form.cleaned_data['tablesize']
		#slot=form.cleaned_data['slot']
		#ob.slot=slot
		#ob.save()
		#form.save()

		#messages.success(request,'Congratulations.. your Resevation has been updated. Please Login again to verify')
		#return redirect('account:homepage')
	context={
		  "instance":instance,
		  "form":form
	}
	return render(request,'reservations/cust_edit_reserve.html',context)



def customer_edit_reserve_view(request,oid):
	x=checkout.objects.filter(ord_id=oid).exists()
	oid=oid
	if not x:
		instance=get_object_or_404(Appointment,order_id=oid)
		ob=Appointment.objects.get(order_id=oid)
		form=app(request.POST or None,instance=instance)
		if form.is_valid():
			error=[]
			instance=form.save(commit=False)
			date=form.cleaned_data['date']
			slot=form.cleaned_data['slot']
			restname=instance.tablename_restaur
			restslug=instance.tablename_slug
			ob1=setting.objects.get(restaur_slug=restslug)
			if(str(date)<str(date.today())):
				error.append('Please enter a future date')
			if len(Appointment.objects.filter(date = date ,slot=slot,tablename_restaur=restname)) >= ob1.no_of_reservations_per_hour:
				error.append("Oops!! Opted Time Slot is full, Please enter different Slot")
			if(str(slot)<str(datetime.now().strftime("%H:%M")) and str(date)<=str(date.today())):
				error.append('Please enter a future time slot')
			if len(error)>0:
				for each in error:
					messages.error(request,each)
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			if(len(error)==0):
				instance.save()
				messages.success(request,'Congratulations.. your Resevation has been updated. Please Login again to verify')
				return redirect('account:homepage')
		context={
		"instance":instance,
		"form":form
		}
		return render(request,'reservations/cust_edit_reserve.html',context)

	else:
		x=Appointment.objects.get(order_id=oid)
		rest=restaurant_details.objects.get(Restaurant_name=x.tablename_restaur,slug=x.tablename_slug)
		obj=Appointment.objects.get(order_id=oid)
		crt =cart.objects.filter(oid=oid)
		check=checkout.objects.get(ord_id=oid)
			
				
		messages.error(request,'Cannot Edit ,The food is already ordered')
		return render(request,'reservations/customer_tablereserve_check.html',{'oid':oid,'rest':rest,'obj':obj,'crt':crt,'check':check})


def order(request,slug1,slug2):
	obj=menu.objects.filter(rest_menu_slug=slug1,menu_type='veg_starter')
	obj1=menu.objects.filter(rest_menu_slug=slug1,menu_type='veg_maincourse')
	obj2=menu.objects.filter(rest_menu_slug=slug1,menu_type='nonveg_starter')
	obj3=menu.objects.filter(rest_menu_slug=slug1,menu_type='nonveg_maincourse')
	obj4=menu.objects.filter(rest_menu_slug=slug1,menu_type='Beverages')
	obj5=menu.objects.filter(rest_menu_slug=slug1,menu_type='vodka')
	obj6=menu.objects.filter(rest_menu_slug=slug1,menu_type='redwine')
	obj7=menu.objects.filter(rest_menu_slug=slug1,menu_type='veg_chinese')
	obj8=menu.objects.filter(rest_menu_slug=slug1,menu_type='nonveg_chinese')
	obj9=menu.objects.filter(rest_menu_slug=slug1,menu_type='wine')
	obj10=menu.objects.filter(rest_menu_slug=slug1,menu_type='beer')
	obj11=menu.objects.filter(rest_menu_slug=slug1,menu_type='pizza')
	obj12=menu.objects.filter(rest_menu_slug=slug1,menu_type='burger')
	obj13=menu.objects.filter(rest_menu_slug=slug1,menu_type='dessert')
	ob=cart.objects.filter(oid=slug2)
	ob1=Appointment.objects.get(order_id=slug2)
	slug=slug2
	error=[]
	newtime=ob1.slot
	presenttime=datetime.now().strftime("%H:%M")
	frmt="%H:%M"
	restime=datetime.strptime(newtime,frmt)-datetime.strptime(presenttime,frmt)

	if str(restime)>str(1) or str(date)>=str(date.today()):
		objet=menu.objects.filter(rest_menu_slug=slug1)
		return render(request,'reservations/order.html',{'obj':obj,'slug':slug,'ob':ob,'obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4,'obj5':obj5})

   

	else:
		messages.error(request,'Your Resevation time is near, cannot order food,Time limit should be atleast Two hours ')
		messages.error(request,'Please edit your Reservation timings')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			
  

def cart_view(request,itemid,slug):
	obj=menu.objects.get(menu_id=itemid)
	o=cart.objects.filter(menu_id=itemid,oid=slug).exists()
	if request.GET.get('increase'):
		#var=request.GET.get('increase')
		obj1 = cart.objects.get(menu_id=itemid,oid=slug)
		obj1.quantity=obj1.quantity+1
		obj1.save()

	if request.GET.get('decrease'):
		#var=request.GET.get('increase')
		obj1 = cart.objects.get(menu_id=itemid,oid=slug)
		obj1.quantity=obj1.quantity-1
		if obj1.quantity==0:
			obj1.delete()
		else:
			obj1.save()

	if not o:
		cart.objects.create(oid=slug,menu_id=itemid,price=obj.price,rest_menu_slug=obj.rest_menu_slug,item_name=obj.item,item=obj)



	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 

def checkout_view(request,sl):
	ob=cart.objects.filter(oid=sl)
	obj=Appointment.objects.get(order_id=sl)
	o=checkout.objects.filter(ord_id=sl).exists()
	pr=0
	for i in ob:
		pr=pr+(i.price*i.quantity)
	tax=decimal.Decimal(0.05)*pr
	tax=round(tax,2)
	total=pr+tax
	amount_to_be_paid=decimal.Decimal(0.2)*total
	amount_to_be_paid=round(amount_to_be_paid,2)
	if not o:
		checkout.objects.create(ord_id=sl,f_ord_id=obj,cart_price=pr,tax=tax,total=total,amount_paid=amount_to_be_paid)

	return render(request,'reservations/checkout.html',{'ob':ob,'obj':obj,'pr':pr,'tax':tax,'total':total,'amount_to_be_paid':amount_to_be_paid})


def payment_view(request,ordid):
	ob=checkout.objects.get(ord_id=ordid)
	ob.payment=True
	ob.save()
	if ob.payment:
		ob.amount_due=ob.total-ob.amount_paid
		ob.save()
	return redirect('account:homepage')


def cartdelete_view(request,item_id,ord_slug):
	ob=cart.objects.get(menu_id=item_id,oid=ord_slug)
	ob.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def review_view(request,revordid):
	x=request.POST.get("name")
	y=request.POST.get("review")
	ob=review.objects.filter(review_ordid=revordid).exists()
	if not ob:
		last_app=Appointment.objects.last()
		review.objects.create(name=x,review=y,review_ordid=revordid,review_slug=last_app.tablename_slug)
		
		o=review.objects.filter(review_slug=last_app.tablename_slug)
		return render(request,'reservations/success.html',{'revordid':revordid,'o':o,'last_app':last_app})


		
	else:
		messages.error(request,'Your Review is already added')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def chat_view(request,chatordid):
	x=request.POST.get("name")
	y=request.POST.get("review")
	chat.objects.create(name=x,review=y,review_ordid=chatordid)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



	

