from django import forms
from django.forms import ModelForm
from .models import Article
from tinymce.widgets import TinyMCE

class ArticleModelForm(ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Article
        fields = [ 'title', 'slug', 'cover', 'content' ]