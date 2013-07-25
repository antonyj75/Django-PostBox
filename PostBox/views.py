# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text = "Welcome to the Feedback Postal Service!"
    context = { 'text': text }
    return render(request, 'PostBox/index.html', context)
