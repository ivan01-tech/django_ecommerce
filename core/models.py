from django.db import models
from django.conf import settings
from django.shortcuts import resolve_url, reverse

# resolve_url

LABEL_CHOICES = (
    ("P", "primary"),
    ("S", "secondary"),
    ("D", "danger"),
)

CATEGORY_CHOICES = (
    ("SH", "SHIRT"),
    ("SW", "Sport Wear"),
    ("OW", "Outwear"),
    ("TO", "Tools"),
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, default="SH", max_length=40)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=40)
    slug = models.SlugField()
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse(
            "core:item",
            kwargs={
                "slug": self.slug,
            },
        )

    def get_add_to_cart(self):
        return reverse(
            "core:add-to-cart",
            kwargs={
                "slug": self.slug,
            },
        )

    def get_orders(self):
        return self.orders.filter(item=self)[0].quantity


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(to=OrderItem)

    def __str__(self) -> str:
        return self.user.username
