# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    label = models.CharField(verbose_name='Category', max_length=30)

    def __unicode__(self):
        return self.label

        class Meta:
            verbose_name = 'Categories de jean-kevin'

class Post(models.Model):
    title = models.CharField(verbose_name='Le nom du truc euh post', max_length=30)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField(verbose_name='Textttt')
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Article de jean-kevin'
