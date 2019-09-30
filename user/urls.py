from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path("login/", user_view.Login, name="login"),
    path("register/", user_view.register, name="register"),
    path("logout/", auth.LogoutView.as_view(template_name="wall/wall.html"), name="logout"),
]

