from __future__ import unicode_literals

from django.shortcuts import render


def homepage(request):
    return render(request, 'static_pages/homepage.html')
