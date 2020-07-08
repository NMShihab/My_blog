from django import forms
from Blog.models import Comment,Blog

class CommentForm(forms.ModelForm):
    class  Meta:
        model = Comment
        fields = ('comment',)
        
