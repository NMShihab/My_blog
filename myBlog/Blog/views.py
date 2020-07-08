from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DetailView,ListView,DetailView,TemplateView,View
from Blog.models import Blog
from  django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Blog.form import CommentForm
import uuid


# Create your views here.

# def blog_list(request):
#     return render(request,'Blog/blog_list.html',context={})


class Blog_list(ListView):
    context_object_name = 'Blogs'
    model = Blog
    template_name = 'Blog/blog_list.html'

    # for desending prder
    #queryset = Blog.objects.order_by('-publish_date')


class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'Blog/create_blog.html'
    fields =('blog_title','blog_content','blog_image',)

    def form_valid(self,form):
        blog_object = form.save(commit = False)
        blog_object.author = self.request.user
        title = blog_object.blog_title
        blog_object.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_object.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog:blog_details',kwargs={'slug':slug}))
    return render(request,'Blog/blog_details.html',context={'blog':blog,'comment_form':comment_form})
