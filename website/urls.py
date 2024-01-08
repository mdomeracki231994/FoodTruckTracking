from django.urls import path

from website import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
]
