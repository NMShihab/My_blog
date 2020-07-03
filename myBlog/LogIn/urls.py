from django.urls import path
from LogIn import views

app_name = 'LogIn'

urlpatterns =[
path('SignUp/',views.SignUp,name='signup'),
path('LogIn/',views.LogIn,name='login'),
path('LogOut/',views.logout_user,name='logout'),
path('Profile/',views.user_profile,name='profile'),
path('Change_profile/',views.change_profile,name='change_profile'),
path('password/',views.pass_change,name ='pass_change')

]
