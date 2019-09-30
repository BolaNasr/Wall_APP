from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    # that for CRUD posts
    path("new", views.post_create, name="post_new"),
    path("edit/<int:pk>", views.post_update, name="post_edit"),
    path("delete/<int:pk>", views.post_delete, name="post_delete"),
]
