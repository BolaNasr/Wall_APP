from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Create your views here.


def register(request):
    """
    register new user
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            # for send welcome mail
            Email_template = get_template("user/Email.html")
            data = {"username": username}
            subject, from_email, to = "welcome", "bola.e.nasr@gmail.com", email
            html_content = Email_template.render(data)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, "Congratulaions, Your account has been created ")
            return redirect("user/login")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form, "title": "Welcome , Register please"})


def Login(request):
    """
    login for user
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f" Welcome {username} .. !!")
            return redirect("/")
        else:
            messages.info(request, f"incorrect username or password")
    form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form, "title": "log in"})


def index(request):
    """
    render wall html
    """
    return render(request, "wall/wall.html", {"title": "index"})
