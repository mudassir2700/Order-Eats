from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from . models import restaurant_details,setting
from reservations.models import Appointment
# Create your views here.
from django.contrib import messages
from .forms import Rest_Info,res_info
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms
from django.urls import reverse
from menu.models import menu 

@login_required(login_url="account:login")
def resthomepage_view(request):
	return render(request,'rest_details/resthomepage.html')

@login_required(login_url="account:login")	
def restdetail_view(request):
	if request.method=='POST':
		form=forms.Rest_Info(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.owner=request.user
			
			instance.save()
			slug=instance.slug
			messages.success(request,'Congratulations, you have created your Restaurant on Order-Eat')

			return render(request,'rest_details/res.html',{'slug':slug})
	else:
		form=forms.Rest_Info()
	return render(request,'rest_details/restdetail.html',{'form':form})

@login_required(login_url="account:login")	
def restview_view(request):
	ob=restaurant_details.objects.filter(owner=request.user)
	return render(request,'rest_details/restview.html',{'ob':ob})

@login_required(login_url="account:login")	
def tablereserve_view(request,slug):
	res=Appointment.objects.filter(tablename_slug=slug)
	appoint=restaurant_details.objects.get(slug=slug)
	return render(request,'rest_details/table_reserve.html',{'res':res,'appoint':appoint})

@login_required(login_url="account:login")	
def restupdate_view(request,slug):
	instance=get_object_or_404(restaurant_details,slug=slug)
	form=forms.Rest_Info(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.owner=request.user
		instance.save()
		messages.success(request,'Restaurant Details have beeen successfully updated')
		return redirect('restinfo:resthomepage')
	context={
	      "instance":instance,
	      "form":form
	}
	return render(request,'rest_details/rest_update.html',context)


def no_of_rest_update_view(request):
	ob=restaurant_details.objects.filter(owner=request.user)
	return render(request,'rest_details/no_of_rest_update.html',{'ob':ob})

def no_of_setting_view(request,slug):
	ob=restaurant_details.objects.get(slug=slug)
	if request.method=='POST':
		form=forms.res_info(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.restaur_name=ob
			instance.restaur_slug=ob.slug
			instance.save()
			#messages.success(request,'Congratulations, you have created your Restaurant on Order-Eat')
			return redirect('restinfo:no_of_restupdatdetail')
	else:
		form=forms.res_info()
	return render(request,'rest_details/reserve.html',{'form':form})

def reserve_settings_view(request,slug):
	instance=get_object_or_404(setting,restaur_slug=slug)
	ob=restaurant_details.objects.get(slug=slug)
	form=forms.res_info(request.POST or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.restaur_name=ob
		instance.restaur_slug=ob.slug
		instance.save()
		return redirect('restinfo:resthomepage')
	else:
		context={
		"instance":instance,
		"form":form
		}
	return render(request,'rest_details/reservation_settings.html',context)

def reserve_setting_view(request,slug):
	ob=restaurant_details.objects.get(slug=slug)
	x=request.POST.get("minres")
	y=request.POST.get("maxres")
	z=request.POST.get("nores")
	setting.objects.create(minimum_party_size=x,maximum_party_size=y,no_of_reservations_per_hour=z,restaur_name=ob,restaur_slug=ob.slug)

	return redirect('restinfo:resthomepage')

@login_required(login_url="account:login")	
def restmenu_view(request):
	ob=restaurant_details.objects.filter(owner=request.user)
	return render(request,'rest_details/menuupdate.html',{'ob':ob})

def menuview_view(request,slg):
	o=menu.objects.filter(rest_menu_slug=slg)
	return render(request,'rest_details/menuview.html',{'o':o,'slg':slg})


def menuadd_view(request,menuslug):
	
	if request.method=='POST':
		obj=restaurant_details.objects.get(slug=menuslug)
		form=forms.menu_infoadd(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.rest_menu_slug=menuslug
			instance.rest_menu=obj
			instance.save()
			slg=menuslug
			messages.success(request,'Congratulations, you have added menu')

			return redirect('restinfo:resthomepage')
	else:
		form=forms.menu_infoadd()
	return render(request,'rest_details/menuadd.html',{'form':form})


def menuedit_view(request,itemid):
	instance=get_object_or_404(menu,menu_id=itemid)
	ob=menu.objects.get(menu_id=itemid)
	o=menu.objects.filter(rest_menu_slug=ob.rest_menu_slug)
	form=forms.menu_info(request.POST or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.owner=request.user
		instance.save()
		messages.success(request,'Menu Details have beeen successfully updated')
		return redirect('restinfo:resthomepage')
	context={
	      "instance":instance,
	      "form":form,
	      "o":o,
	      "itemid":itemid,
	}

	return render(request,'rest_details/menuupdation.html',context)

def menudelete_view(request,itemid1):
	ob=menu.objects.get(menu_id=itemid1)
	ob.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
