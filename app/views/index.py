from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.decorators.cache import cache_page

from app.forms.test_login_form import LoginForm, SignupForm


@login_required
def index(request):
    success = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            print(email, password)
            success = True
    else:
        form = LoginForm()

    rendering_info = dict(
        title="Home",
        user_id=1,
        date_joined=datetime(2022, 1, 1, 0, 0, 0),
        category_list=[1, 2, 3],
        price=1000,
        note=None,
        msg="Hello World",
        java="Java",
        python="Python",
        success=success,
        form=form,
    )

    return render(request, "index.html", rendering_info)


def user_signup(request):
    return render(request, "signup.html")


def user_signup2(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = SignupForm()

    return render(request, "signup2.html", {"form": form})


def user_login(request):
    msg = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = form.cleaned_data.get("email_or_username")
            password = form.cleaned_data.get("password")

            user = User.objects.filter(Q(email=email_or_username) | Q(username=email_or_username)).first()
            if not user:
                msg = "로그인 정보가 올바르지 않습니다.."
            else:
                valid_password = check_password(password, user.password)
                if not valid_password:
                    msg = "로그인 정보가 올바르지 않습니다.."
                else:
                    login(request, user)
                    return redirect("index")
    else:
        if request.user.is_authenticated:
            return redirect("index")
        form = LoginForm()

    return render(request, "login.html", {"form": form, "msg": msg})


def user_logout(request):
    logout(request)
    return redirect("login")


def cache_test(request):
    from django.shortcuts import render
    from django.core.cache import cache

    user = cache.get("user_query_cache")
    if user is None:
        user = User.objects.all()
        cache.set("user_query_cache", user, 3600)
        print("query executed!!!!!!")

    # Perform the expensive database query here
    return render(request, "cache_test.html", {"user": user})


# @cache_page(3600)
def cache_test2(request):
    result = dict(
        title="CacheTest",
        user_id=1,
        date_joined=datetime(2022, 1, 1, 0, 0, 0),
    )
    return render(request, "cache_test2.html", {"result": result})
