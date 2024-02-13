from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quote


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context = {"quotes" : quotes_on_page} )
