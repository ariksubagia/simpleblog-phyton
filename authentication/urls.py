from .views import login_page, signout
from django.urls import path

urlpatterns = [
    path('signin/', login_page, name='signin'),
    path('signout/', signout, name='signout')
]