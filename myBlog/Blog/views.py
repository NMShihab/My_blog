from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DetailView,ListView,DetailView,TemplateView,View
from Blog.models import Blog ,Comment, Likes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Blog.forms import CommentForm
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
    already_liked = Likes.objects.filter(blog=blog,user= request.user)
    if already_liked:
        liked = True
    else:
        liked = False

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog:blog_details',kwargs={'slug':slug}))
    return render(request,'Blog/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})

@login_required
def liked(request,pk):

    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user = user)

    if not already_liked:
        liked_post = Likes(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('Blog:blog_details',kwargs={'slug':blog.slug}))


@login_required
def unliked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user = user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog:blog_details',kwargs={'slug':blog.slug}))
