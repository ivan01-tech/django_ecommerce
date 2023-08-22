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


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
