
# from bson.objectid import ObjectId
from django.shortcuts import  get_object_or_404
from django import template
from ..models import Author, Tag
from django.db.models import Count


register = template.Library()


def get_author(id_):
    author = get_object_or_404(Author, id = id_)
    return author.fullname


def get_tags(id_):
    tags = Tag.objects.filter(quote = id_).all()
    return tags


def toptentags(_):
    toptags = Tag.objects.annotate(quote_count=Count('quote')).order_by('-quote_count')[:10] # DESC LIM10
    return toptags


register.filter('toptags', toptentags)
register.filter('tags', get_tags)
register.filter('author', get_author)











