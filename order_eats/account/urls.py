from django.urls import path,include
from.import  views
from django.conf.urls import url
app_name='account'
urlpatterns = [
     path('',views.homepage,name='homepage'),
     path('signup/',views.signup,name='signup'),
     path('albertdream/',views.albertdream,name='albert'),
     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
     url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
     path('resthome/',include('rest_details.urls',namespace='restinfo')),
     path('login/',views.login_view,name='login'),
     path('logout/',views.logout_view,name='logout'),
     #url(r'^cuisine/(?P<cuisine_type>[\w-]+)/$',views.cuisine_view,name='cuisine'),
     url(r'^resmain/(?P<slug>[\w-]+)/$',views.reserve_view,name='reserve'),
     #url(r'^(?P<cuisine_type>[\w-]+)/$',views.cuisine_view,name='cuisine'),
     path('cuisine/<cuisine_type>',views.cuisine_view,name='cui'),
     path('filter/',views.filter_view,name='filter'),
     path('casual-dining',views.casual_dining_view,name='casual_dining'),
     path('fine-dining',views.fine_dining_view,name='fine_dining'),
     path('bar',views.bar_view,name='bar'),
     path('cafe',views.cafe_view,name='cafe'),
     path('food-court',views.food_court_view,name='food_court'),
     path('bakeries',views.bakery_view,name='bakeries'),
     path('reservations/',include('reservations.urls',namespace='reservations')),
     path('previous/',views.previous,name='previous'),
     path('about-dhanush/',views.aboutdhanush,name='aboutdhanush'),
     #url(r'^(?P<slug>[\w-]+)/(?P<cuisine_type>[\w-]+)/$',views.cuisine_view,name='cuisine'),
     #url(r'^cuis/(?P<cuisine_type>[\w-]+)/cuis1/(?P<slug>[\w-]+)/$',views.res_view,name='res'),


    

    
   
]
