from datetime import datetime

from django.contrib.auth import logout, authenticate, login

from django.shortcuts import render, redirect

from app.forms.test_login_form import LoginForm, SignupForm


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
