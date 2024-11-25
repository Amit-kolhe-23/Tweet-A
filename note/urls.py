from django.urls import path
from.views import*

urlpatterns = [
    path("",home,name="home"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path("register/",register,name="register"),
    path("create/",tweet_create, name="tweet_create"),
    path("edit/<int:tweet_id>",tweet_edit, name="tweet_edit"),
    path("delete/<int:tweet_id>",tweet_delete, name="tweet_delete"),
]
    