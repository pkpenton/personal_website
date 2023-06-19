from django.urls import re_path
# from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    re_path(r'^$', views.homepage, name='homepage'),
    re_path(r'resume/', views.resume, name='resume'),
    re_path(r'^about/', views.about, name='about'),
    re_path(
        r'^favicon.ico$',
        RedirectView.as_view(
            url="/static/favicon.ico",
            permanent=False),
        name="favicon"
    ),
]
