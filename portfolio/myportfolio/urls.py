from django.urls import path
from .views import *
app_name = 'myportfolio'
urlpatterns = [
    path('', Homepage, name = 'homepage'),
    path('home', Homepage, name = 'homepage'),
    path('about', Aboutpage, name = 'aboutpage'),
    path('contact', Contactpage, name = 'contactpage'),
    path('projects', Myprojects, name = 'myprojects'),
    path('resume', Myresume, name='myresume'),
]