from django.contrib.auth import login, authenticate,logout
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_details.models import restaurant_details,setting
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.db.models import Q
from django.contrib import messages


def homepage(request,*args,**kwargs):
	obj=restaurant_details.objects.filter(status='accepted').order_by('cuisine_type')
	ob=restaurant_details.objects.all()
	lst=[]
	for i in obj:
		if(i in lst):
			lst.append(i)

	#print(lst)
	return render(request,'account/ho.html',{'obj':obj,'lst':lst,'ob':ob})

def albertdream(request):
	return render(request,'account/j_qeury.html')
def aboutdhanush(request):
	return render(request,'account/about_responsive.html')


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			#username = form.cleaned_data.get('username')
			#raw_password = form.cleaned_data.get('password1')
			#user = authenticate(username=username, password=raw_password)
			#login(request, user)
			user = form.save(commit=False)
			user.is_active = False
			user.save()

			current_site = get_current_site(request)
			subject = 'Activate Your Order-Eat Account'
			message = render_to_string('account/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			from_email = settings.EMAIL_HOST_USER
			to_list = [to_email,settings.EMAIL_HOST_USER]
			send_mail(
						subject, message, from_email,to_list,fail_silently=True
			)
			return redirect('account:account_activation_sent')
	else:
		form = SignUpForm()
	return render(request, 'account/sign.html', {'form': form})

def account_activation_sent(request):
	return render(request, 'account/account_activation_sent.html')


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		#user.profile.email_confirmed = True
		user.save()
		login(request, user)
		return redirect('restinfo:resthomepage')
	else:
		return render(request, 'account/account_activation_invalid.html')


def login_view(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			#us=User.objects.all()
			login(request,user)
			if 'next' in request.POST:
				return redirect('restinfo:resthomepage')
			else:
				return redirect('restinfo:resthomepage')

	else:
		form = AuthenticationForm()

	return render(request,'account/login.html',{'form':form})

def logout_view(request):
	logout(request)	
	return redirect('/') 

@login_required(login_url="account:login")	
def create_view(request):
	return render(request,'account/create.html')


def reserve_view(request,slug):
	ob=restaurant_details.objects.get(slug=slug)
	return render(request,'account/reserve.html',{'ob':ob})

def cuisine_view(request,cuisine_type):
	o=restaurant_details.objects.filter(
		Q(cuisine_type__icontains=cuisine_type)|
		Q(Cuisines_You_Offer__icontains=cuisine_type)|
		Q(Restaurant_name__icontains=cuisine_type)
		)
	
	return render(request,'account/cuisine.html',{'o':o})

def res_view(request,slug):
	ob=restaurant_details.objects.get(slug=slug)
	return render(request,'account/reserve.html',{'ob':ob})

def filter_view(request):
	query=request.GET.get('q')
	ob=restaurant_details.objects.filter(status='accepted').filter(
		Q(cuisine_type__icontains=query)|
		Q(Cuisines_You_Offer__icontains=query)|
		Q(Restaurant_name__icontains=query)
		)
	if not ob:
		messages.error(request,'Sorry, the restaurent is not available')

	return render(request,'account/filter.html',{'ob':ob})

def casual_dining_view(request):
	q=request.GET.get("fil")
	if q:
		qry=restaurant_details.objects.filter(status='accepted').filter(Type_of_dining__icontains='Casual').filter(Cuisines_You_Offer__icontains=q)
	else:
		qry=restaurant_details.objects.filter(status='accepted').filter(Type_of_dining__icontains='Casual')

	
	return render(request,'account/casual.html',{'qry':qry})

def fine_dining_view(request):
	qry=restaurant_details.objects.filter(status='accepted').filter(Type_of_dining__icontains='fine')
	return render(request,'account/fine.html',{'qry':qry})

def bar_view(request):
	qry=restaurant_details.objects.filter(status='accepted').filter(Type_of_dining__icontains='bar')
	return render(request,'account/bar.html',{'qry':qry})

def cafe_view(request):
	qry=restaurant_details.objects.filter(status='accepted').filter(Type_of_dining__icontains='cafe')
	return render(request,'account/cafe.html',{'qry':qry})

def food_court_view(request):
	qry=restaurant_details.objects.filter(status='accepted').filter(
		Q(Type_of_dining__icontains='food ')|
		Q(Type_of_dining__icontains='court')
		)
	return render(request,'account/food_court.html',{'qry':qry})

def bakery_view(request):
	qry=restaurant_details.objects.filter(status='accepted').filter(Type_of_dining__icontains='bake')
	return render(request,'account/bakery.html',{'qry':qry})

def previous(request):
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))