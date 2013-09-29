from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Feedback(models.Model):
    example = models.TextField(null=True, blank=True, verbose_name='Provide example of the observed behavior:',
                               help_text='Describe the observed behavior.')
    consequence = models.TextField(null=True, blank=True,
                                   verbose_name='Impact or Consequence of the observed behavior:',
                                   help_text='Describe the consequence of the observed behavior.')
    suggestion = models.TextField(verbose_name='My suggestion to improve or change the behavior:',
                                  help_text='Provide the feedback suggestion for improvement.')
    date = models.DateTimeField()
    user = models.ForeignKey(User, verbose_name='Feedback Receiver')
    sender = models.CharField(max_length=30, null=True, blank=True, verbose_name='Feedback Sender',
                              help_text='Your feedback is anonymous. \
                              But you can put your name here in case you want the manager know who sent the feedback.')

    def __str__(self):
        return "Feedback to " + self.user.username
