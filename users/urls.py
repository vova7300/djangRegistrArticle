from django.urls import path
from . import views
from .models import Articles
from django.views.generic import ListView


urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("article_list", ListView.as_view(queryset=Articles.objects.all().order_by("-date")), name="article_list")
]