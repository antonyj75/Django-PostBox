# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

#def index(request):
#    return render(request, 'PostBox/index.html')

def selection(request):
    try:
        selected_choice = request.GET['choice']
    except KeyError:
        # Display the same form
        return render(request, 'PostBox/index.html', {'error_message': 'Please select what you want to post.'})
    return HttpResponseRedirect(reverse('PostBox:thankyou'))
    #return HttpResponse("You're making a selection")

def thankyou(request):
    return render(request, 'PostBox/thankyou.html', {'choice':'1'})
