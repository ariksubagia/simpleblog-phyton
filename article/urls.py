from django.urls import path
from .views import article_index,article_single,article_add,article_edit

urlpatterns = [
    path('', article_index, name="articles"),
    path('article/new/', article_add, name="article_add"),
    path('article/<str:slug>/edit', article_edit, name="article_edit"),
    path('article/<str:slug>/', article_single, name="article_single"),
]