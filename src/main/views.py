from uuid import uuid1
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from .models import Story, Author, Word

def index(request):
    return read(request)

def read(request):
    top5 = Story.objects.order_by('-score')[:5]
    template = loader.get_template('read.html')
    context = RequestContext(request, {
        'top5': top5,
    })
    return HttpResponse(template.render(context))

def write(request, story_id = ""):
    template = loader.get_template('write.html')
    try:
        sid = int(story_id)
    except ValueError:
        sid = 0

    try:
        story = Story.objects.get(pk=sid)
    except Story.DoesNotExist:
        sid = 0
        story = {}

    context = RequestContext(request, {
        'isRead': False,
        'id': sid,
        'story': story,
        'uuid': request.session.get('author_id','')
    })
    return HttpResponse(template.render(context))

def new(request):

    story = Story(
        text = '',
        completed = False,
        score = 5,
    )

    story.save()

    author = Author(
        user = User.objects.get(pk=1),
        story = story,
        order = 0,
        uuid = uuid1().__str__()
    )

    author.save()

    id = story.id
    request.session['author_id'] = author.uuid
    url = '/story/write/'+str(id)

    return redirect(url)

def join(request):
    id = 0
    url = '/story/write/'+str(id)
    return redirect(url)

def addWord(request):
    word = Word(
        text = '',
        author = Author.objects.get(
            uuid = request.session.get('author_id','')
        ),
    )

    word.save()