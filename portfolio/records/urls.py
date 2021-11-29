from django.urls import path

from .views import TestView

app_name = "users"
urlpatterns = [
    path("", view=TestView.as_view(), name="show_all"),
]
