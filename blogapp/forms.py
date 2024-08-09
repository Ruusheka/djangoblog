from blogapp.models import MyBlog
from django import forms # type: ignore


class BlogForm(forms.ModelForm):
    class Meta:
        model=MyBlog
        fields='__all__'
        