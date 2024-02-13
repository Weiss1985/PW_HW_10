from django.shortcuts import render
from quotes.models import Tag, Quote
from django.db.models import Count


def main(request, tag=""):
    tag = Tag.objects.get(name=tag)
    quotes = Quote.objects.filter(tags=tag)
    return render(request, "tags/tags.html", context = {'quotes': quotes, "tags":tag})


def toptentags(request):
    toptags = Tag.objects.annotate(quote_count=Count('quote')).order_by('-quote_count')[:10] # DESC LIM10
    return render(request, 'tags/toptentags.html', context={"toptags":toptags })