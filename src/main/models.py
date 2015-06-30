from django.db import models
from django.contrib.auth.models import User
from uuid import uuid1


class Story(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(verbose_name=u"Time",auto_now=True)
    score = models.IntegerField(default=5)
    def __str__(self):
        return self.text


class Author(models.Model):


    user = models.ForeignKey(User)
    story = models.ForeignKey(Story)
    order = models.IntegerField(default=0)
    uuid = models.CharField(max_length=64,default='' )

    def __str__(self):
        return self.user.__str__()


class Word(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User,verbose_name=u"Author")
    story = models.ForeignKey(Story,verbose_name=u"Story ")
    time = models.DateTimeField(verbose_name=u"Time",auto_now=True)

    def __str__(self):
        return self.text
