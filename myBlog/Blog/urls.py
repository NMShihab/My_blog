from django.urls import path
from Blog import views

app_name = 'Blog'

urlpatterns =[
    path('',views.blog_list,name='blog_list'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
]
