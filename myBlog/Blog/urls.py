from django.urls import path
from Blog import views

app_name = 'Blog'

urlpatterns =[
    path('',views.Blog_list.as_view(),name='blog_list'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<slug:slug>',views.blog_details,name='blog_details'),
    path('liked/<pk>/',views.liked,name='liked_post'),
    path('unliked/<pk>/',views.unliked,name='unliked_post'),

]
