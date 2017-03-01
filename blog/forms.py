from django import forms
from .models import Post

# form with title and content fields corresponding to Post model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')