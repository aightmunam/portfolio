"""
All the views for the records app
"""

from django.http import HttpResponse
from django.views.generic import View


class TestView(View):
    def get(self, request):
        return HttpResponse("This is just a test view")
