from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from core.models import Item, Order, OrderItem
from django.views.generic import ListView, DetailView
from django.utils.timezone import now


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


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.get_or_create(item=item)[0]
    user = request.user
    order_qs = Order.objects.filter(user=user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            print("order : ", order_item)
            order.items.add(order_item)
    else:
        order = Order.objects.create(
            user=request.user,
            ordered_date=now(),
        )
        order.items.add(order_item)
    return redirect("core:item", slug=slug)
