from django.urls import path,include
from .import views
from django.conf.urls import url
app_name='restinfo'
urlpatterns=[
     path('',views.resthomepage_view,name='resthomepage'),
     path('create/',views.restdetail_view,name='restdetail'),
     path('view/',views.restview_view,name='restviewdetail'),
     path('edit/',views.no_of_rest_update_view,name='no_of_restupdatdetail'),
     path('menu/',views.restmenu_view,name='restmenudetail'),
     url(r'^edit/(?P<slug>[\w-]+)/$',views.restupdate_view,name='restupdatedetail'),
     url(r'^tableview/(?P<slug>[\w-]+)/$',views.tablereserve_view,name='table_reserve_view'),
     url(r'^set/(?P<slug>[\w-]+)/$',views.no_of_setting_view,name='no_of_setting_view'),
     url(r'^settings/(?P<slug>[\w-]+)/$',views.reserve_settings_view,name='settings_view'),
     url(r'^setting/(?P<slug>[\w-]+)/$',views.reserve_setting_view,name='setting_view'),
     url(r'^menu-view/(?P<slg>[\w-]+)/$',views.menuview_view,name='menuviewdetail'),
     url(r'^menu-edit/(?P<itemid>[\w-]+)/$',views.menuedit_view,name='menuedit'),
     url(r'^menu-add/(?P<menuslug>[\w-]+)/$',views.menuadd_view,name='menuadd'),
     url(r'^menu-delete/(?P<itemid1>[\w-]+)/$',views.menudelete_view,name='menudelete'),


     


]