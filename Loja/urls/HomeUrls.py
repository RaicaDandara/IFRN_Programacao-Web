from django.urls import path
from Loja.views.HomeView import home_view
urlpatterns = [
    path("", home_view, name= 'home'),
]