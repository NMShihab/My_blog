from django.urls import path
from LogIn import views

app_name = 'LogIn'

urlpatterns =[
path('SignUp/',views.SignUp,name='signup')

]
