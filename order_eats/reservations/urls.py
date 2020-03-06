from django.conf.urls import url
from . import views
from django.urls import path

app_name='reservations'

urlpatterns = [

    path('status/',views.cust_tablereserve_view,name='cust_table_reserve_check'),
    url(r'^tablereserve/(?P<slug>[\w-]+)/$',views.index,name='index'),
    #path('',views.index,name='index'),
    url(r'^tablereservation/(?P<slug>[\w-]+)/$', views.addi,name='addi'),
    url(r'^edit-tablereservation/(?P<oid>[\w-]+)/$', views.customer_edit_reserve_view,name='cust_edit_reserve'),
    url(r'^appoint/$', views.appoint,name='appoint'),
    url(r'^order/(?P<slug1>[\w-]+)/(?P<slug2>[\w-]+)/$',views.order,name='menuorder'),
    url(r'^cart/(?P<itemid>[\w-]+)/(?P<slug>[\w-]+)/$',views.cart_view,name='cart'),
    url(r'^cart-delete/(?P<item_id>[\w-]+)/(?P<ord_slug>[\w-]+)/$',views.cartdelete_view,name='cartitem_delete'),
    url(r'^checkout/(?P<sl>[\w-]+)/$', views.checkout_view,name='checkout'),
    url(r'^payment/(?P<ordid>[\w-]+)/$', views.payment_view,name='payment'),
    url(r'^review//(?P<revordid>[\w-]+)/$', views.review_view,name='revordid'),
    url(r'^chat/(?P<chatordid>[\w-]+)/$', views.chat_view,name='chatordid'),
    
    #url(r'^cart/(?P<item>[\w-]+)/$',views.cart,name='cart'),
   
    #url(r'^update/(?P<appoint_id>\d+)$', views.update),
    #url(r'^logout$', views.logout),
    #url(r'^delete/(?P<appoint_id>\d+)$', views.delete),
    #url(r'^edit_appoint/(?P<appoint_id>\d+)$', views.edit_appoint),
]
