from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('home/', views.home, name='home'),
    path('api/token/', views.token_login, name='token_login'),
    path('api/hello', views.hello, name='hello'),
]
