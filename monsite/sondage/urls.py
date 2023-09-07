from django.urls import path

from . import views
app_name = 'sondage'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.my_logout, name='logout'),
    path('registered/', views.registered, name='registered'),
    path('welcome/', views.welcome, name='welcome'),
    path('profil/', views.profil, name='profil'),
    path('profil/become', views.become, name='become'),
]
