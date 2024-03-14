from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from quotes.models import Quote, Author


def main(request, author=""):
    a = get_object_or_404(Author, fullname=author)
    return render(request, "authors/authors.html", context = vars(a))
    
