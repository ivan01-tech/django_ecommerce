from django.urls import path
from .views import list_view

app_name = "core"
urlpatterns = [
    path("", list_view, name="list_view"),
]
