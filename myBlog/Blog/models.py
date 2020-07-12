from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model for blog
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=300, verbose_name='Put a title')
    slug = models.SlugField(max_length=300, unique=True)
    blog_content = models.TextField(verbose_name='What is on your mind?')
    blog_image = models.ImageField(upload_to = 'blog_images',verbose_name='Images')
    publish_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)

    class  Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.blog_title


# Model for comment
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_date_update = models.DateTimeField(auto_now=True)

    class  Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return self.comment

# Model for likes

class Likes(models.Model):
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE,related_name='liked_blog')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='liker_user')
