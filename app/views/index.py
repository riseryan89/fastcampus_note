from datetime import datetime

from django.shortcuts import render


def index(request):
    rendering_info = dict(
        title="Home",
        user_id=1,
        date_joined=datetime(2022, 1, 1, 0, 0, 0),
        category_list=[1, 2, 3],
        price=1000,
        note=None,
        msg="Hello World",
    )
    return render(request, "index.html", rendering_info)
