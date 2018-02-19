from django.conf.urls import url
# from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'resume/', views.resume, name='resume'),
    url(r'about/', views.about, name='about'),
    url(
        r'^favicon.ico$',
        RedirectView.as_view(
            url="/static/favicon.ico",
            permanent=False),
        name="favicon"
    ),
]
