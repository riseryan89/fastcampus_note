from datetime import datetime

from django.shortcuts import render

from app.forms.test_login_form import LoginForm


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
