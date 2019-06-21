from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='lider_perfil'),
    path('denuncia/', views.denuncia, name='lider_denuncia'),
    path('autoproteccion/', views.autoproteccion, name='lider_autoproteccion'),
    path('about/', views.about, name='lider_about'),
    # path('registro/', views.registro_view, name='registro'),
    # path('registro/new', views.registrar, name='registrar'),
    # path('home/', views.home, name='home'),
    # path('dashboard/', views.dashboard, name='dashboard'),
]
