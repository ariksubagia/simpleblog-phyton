from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.utils import timezone
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = HTMLField(blank=True, null=True)
    cover = models.ImageField(upload_to='article/', blank=True)
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} | {strip_tags(self.content)[0:150]} ...'

    def summary(self):
        return f'{strip_tags(self.content)[0:150]} ...'

    class Meta:
        db_table = 'articles'