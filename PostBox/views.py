# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from PostBox.models import Feedback
from django.forms import ModelForm
from django.utils import timezone


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

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback

def feedback(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    myfeedback = Feedback(user=user)
    form = FeedbackForm(request.POST, instance=myfeedback)
    if request.method == 'POST':
        if form.is_valid():
            myfeedback.date = timezone.now()
            form.save()
            return redirect('PostBox:success', sender=myfeedback.sender)
    return render(request, 'PostBox/feedback.html', {'user': user, 'form': form,})

def success(request, sender):
    return render(request, 'PostBox/success.html', {'sender':sender})
