from django.urls import path
from .views import add_to_cart, DetailView, HomeView

app_name = "core"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/<slug>/", DetailView.as_view(), name="item"),
    path("products/<slug>/add-to-cart/", add_to_cart, name="add-to-cart"),
]

