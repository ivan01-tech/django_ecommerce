from django.urls import path
from .views import DetailView, HomeView

app_name = "core"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/<slug>/", DetailView.as_view(), name="item"),
]
