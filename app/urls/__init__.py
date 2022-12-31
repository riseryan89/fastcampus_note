from django.urls import include, path

from app.urls import api_urls
from app.urls.render_urls import urlpatterns as render_urls

urlpatterns = [
    path("api/", include(api_urls.urlpatterns)),
] + render_urls
