from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request,'TMweb/home.html')	

def ec(request):
	return render(request,'TMweb/ec.html');

def events(request):
	return render(request,'TMweb/events.html');	

def articles(request):
	return render(request,'TMweb/articles.html');	