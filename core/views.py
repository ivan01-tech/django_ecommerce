from django.shortcuts import render
from core.models import Item

# from django.urllib.request to make request


def list_view(request):
    context = {
        "items": Item.objects.all(),
    }
    return render(request, "list_view.html", context)
