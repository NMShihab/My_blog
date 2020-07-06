from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DetailView,ListView,DetailView,TemplateView,View
from Blog.models import Blog
from  django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid


# Create your views here.

def blog_list(request):
    return render(request,'Blog/blog_list.html',context={})


class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'Blog/create_blog.html'
    fields =('blog_title','blog_content','blog_image',)

    # def form_valid(self,form):
    #     blog_object = form.save(commit = False)
    #     blog_object.author = self.request.user
    #     title = blog_object.blog_title
    #     blog_object.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
    #     blog_object.save()
    #     return HttpResponseRedirect(reverse('index'))
