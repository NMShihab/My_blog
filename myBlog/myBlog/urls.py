
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('LogIn.urls')), # add account url
    path('blog/',include('Blog.urls')), # add blog url
    path('',views.Index,name='index')
]
