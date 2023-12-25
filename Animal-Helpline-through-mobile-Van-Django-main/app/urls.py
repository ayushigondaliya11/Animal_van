from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.menu_baar_final,name='menu_baar_final'),
    path('index',views.index,name='index'),
    path('deadregistration',views.deadregistration,name='deadregistration'),
    path('ngoregistration',views.ngoregistration,name='ngoregistration'),
    path('injuredregistration',views.injuredregistration,name='injuredregistration'),
    path('feedback',views.feedback,name='feedback'),
    path('term_2',views.term_2,name='term_2'),
    path('contactus',views.contactus,name='contactus'),
    path('aboutus',views.aboutus,name='aboutus'),
]
