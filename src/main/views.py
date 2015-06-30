from uuid import uuid1
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.decorators import login_required

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
        authors = Author.objects.filter(story=story.id)
        words = Word.objects.filter(story=story.id)
        context = RequestContext(request, {
            'isRead': False,
            'id': sid,
            'authors': authors,
            'words': words,
            'uuid': request.session.get('author_id','')
        })
        return HttpResponse(template.render(context))

    except Story.DoesNotExist:
        sid = 0
        story = {}
        text = ""


@login_required()
def new(request):

    story = Story(
        text = '',
        completed = False,
        score = 5,
    )

    story.save()

    author = Author(
        user = request.user,
        story = story,
        order = 0,
        uuid = uuid1().__str__()
    )

    author.save()

    id = story.id
    request.session['author_id'] = author.uuid
    url = '/story/write/'+str(id)

    return redirect(url)

@login_required()
def join(request):
    id = 0
    url = '/story/write/'+str(id)
    return redirect(url)

@login_required()
def add(request):
    if request.method == 'POST':
        story_id = int(request.POST["story_id"])
        if story_id > 0:
            authors = Author.objects.filter(story=story_id)
            words = Word.objects.filter(story=story_id)
            try:
                user = Author.objects.get(story_id=story_id, user=request.user.id)
            except Author.DoesNotExist:
                return HttpResponse("{error:true,msg:\"You don't have access to that.\"",content_type='application/json')
            if len(authors) > 0 and user.order == len(words)%len(authors):

                text = request.POST["text"]
                word = Word(
                    text = text,
                    story_id = story_id,
                    author = request.user,
                )

                word.save()
                return HttpResponse("{error:false}",content_type='application/json')

    return HttpResponse("{error:true,msg:\"You don't have access to that.\"}",content_type='application/json')


def get(request,story_id='0'):
    id = int(story_id)
    if id > 0:
        story = Story.objects.get(pk=id)
        authors = Author.objects.filter(story=story.id)
        words = Word.objects.filter(story=story.id)
        return render(request,template_name='get.html',context={
            "words": words,
            "authors": authors
        },content_type='application/json')


@sensitive_post_parameters()
@csrf_protect
def register(request):
    return render(request, template_name='')