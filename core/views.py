from django.shortcuts import render
from core.models import Item
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "home.html"


def list_view(request):
    context = {
        "items": Item.objects.all(),
    }
    return render(request, "list_view.html", context)


class DetailView(DetailView):
    model = Item
    template_name = "product.html"
    context_object_name = "item"
