from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage/homepage.html')
    # return HttpResponse('Hello, World!')
