
from django.conf.urls import url
from .views import read, write, new, join, add, get

urlpatterns = [
    url(r'^$', read, name='story_index' ),
    url(r'^read$', read, name='story_read' ),
    url(r'^write/?$', write, name='story_write' ),
    url(r'^write/new/?$', new, name='story_new' ),
    url(r'^write/join/?$', join, name='story_join' ),
    url(r'^write/add/?$', add, name='story_add' ),
    url(r'^write/(?P<story_id>[0-9]+)$', write, name='story_write' ),
    url(r'^get/(?P<story_id>[0-9]+)$', get, name='story_get' ),
]