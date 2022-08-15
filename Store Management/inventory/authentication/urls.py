from django .urls import path , include
from . import views

app_name = 'authentication'

urlpatterns=[
    path('', views.show_login, name = 'login page' ),
    path('login', views.user_login , name = 'login'),
    path('logout', views.user_logout , name= 'logout')

]