from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Story

def index(request):
    readObj = read(request)
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'content': readObj.content
    })
    return HttpResponse(template.render(context))

def read(request):
    top5 = Story.objects.order_by('-score')[:5]
    template = loader.get_template('read.html')
    context = RequestContext(request, {
        'top5': top5,
    })
    return HttpResponse(template.render(context))

def write(request):
    top5 = Story.objects.order_by('-score')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'top5': top5,
    })
    return HttpResponse(template.render(context))