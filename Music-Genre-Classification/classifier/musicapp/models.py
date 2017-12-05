# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Song(models.Model):
	name = models.FileField(upload_to='media/')
	# name = models.CharField(max_length= 200)
	genre = models.CharField(max_length = 100, default = "Not identified")
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.name + " - " + sef.genre
