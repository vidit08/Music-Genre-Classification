# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import SongForm

# Create your views here.

def index(request):


	if request.method == 'POST':
		print "received file"
		form = SongForm(request.POST,request.FILES)
		print request
		if form.is_valid():
			print "form is valid"
			form.save()
			return redirect('index')
	else:
		print "start"
		form = SongForm()

	return render(request,'index.html', {'form' : form})