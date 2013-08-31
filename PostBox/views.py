# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def index(request):
    user_list = User.objects.all()
    return render(request, 'PostBox/index.html', {'user_list':user_list})

def selection(request):
    try:
        selected_choice = request.GET['choice']
    except KeyError:
        # Display the same form
        return render(request, 'PostBox/index.html', {
            'error_message': 'Please select what you want to post.',
            'user_list': User.objects.all(),
            })

    user_id = request.GET['user_list']

    if selected_choice == '1':
        return HttpResponseRedirect(reverse('PostBox:thankyou', args=(user_id,)))

    return HttpResponseRedirect(reverse('PostBox:feedback', args=(user_id,)))

def thankyou(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'PostBox/thankyou.html', {'user_name': user.username})

def feedback(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'PostBox/feedback.html', {'user_name': user.username})
