from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "content"]


class PostList(generic.ListView):
    """
    List all posts
    """

    queryset = Post.objects.order_by("-created_on")
    template_name = "wall/wall.html"


class PostDetail(generic.DetailView):
    """
    page of post details
    """

    model = Post
    template_name = "wall/post_details.html"


@login_required
def post_create(request, template_name="wall/post_form.html"):
    """
    Create new post if user logging 
    """
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("/")
    return render(request, template_name, {"form": form})


@login_required
def post_update(request, pk, template_name="wall/post_form.html"):
    """
    update the post who user that logged is created it 
    """

    post = get_object_or_404(Post, pk=pk, author=request.user)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, template_name, {"form": form})


@login_required
def post_delete(request, pk, template_name="wall/post_confirm_delete.html"):
    """
    delete the post who user that logged is created it 
    """
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("/")
    return render(request, template_name, {"object": post})
