from django.urls import path
from LogIn import views

app_name = 'LogIn'

urlpatterns =[
path('SignUp/',views.SignUp,name='signup'),
path('LogIn/',views.LogIn,name='login'),
path('LogOut/',views.logout_user,name='logout')

]
