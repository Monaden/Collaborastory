
from django.conf.urls import url
from .views import read, write

urlpatterns = [
    url(r'^$', read, name='story_index' ),
    url(r'^read$', read, name='story_read' ),
    url(r'^write$', write, name='story_write' ),
]