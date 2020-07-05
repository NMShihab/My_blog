
from django.contrib import admin
from django.urls import path, include
from . import views
# For media Profile
from django.conf import settings
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns,static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('LogIn.urls')), # add account url
    path('blog/',include('Blog.urls')), # add blog url
    path('',views.Index,name='index')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
