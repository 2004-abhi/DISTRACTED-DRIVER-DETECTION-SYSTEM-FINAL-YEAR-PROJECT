from django.urls import path
from ddapp import views

urlpatterns = [
    path('',views.home),
    path('login',views.login),
    #ADMIN
    path('adindex',views.adindex),
    path('adpolice',views.adpolice),
    path('del_pol',views.del_pol),
    #POLICE
    path('polindex',views.polindex),
    path('adtips',views.adtips),
    path('del_tip',views.del_tips),
    path('alert',views.alert),
]
