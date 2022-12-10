from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='accueil'),
    path('nosservices', service, name= 'nosservice'),
    path('detail', detail, name='detail'),
    path('apropos', apropos, name='apropos'),
    path('contact', contact, name='contact')
    
]
