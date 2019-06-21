from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('landing_text/', views.landing_text, name='precios'),
    path('landing_audio/', views.landing_audio, name='precios'),
    # path('registro/', views.registro_view, name='registro'),
    # path('registro/new', views.registrar, name='registrar'),
    # path('home/', views.home, name='home'),
    # path('dashboard/', views.dashboard, name='dashboard'),
]
