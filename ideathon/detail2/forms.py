from django import forms
from .models import Post

class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "main_title",
            "sub_title",
            "contents",
            "created_date",
        ]