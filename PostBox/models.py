from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    example = models.TextField(null=True, blank=True, verbose_name='Provide example of the observed behavior:',
                               help_text='Describe the observed behavior.')
    consequence = models.TextField(null=True, blank=True,
                                   verbose_name='Impact or Consequence of the observed behavior:',
                                   help_text='Describe the consequence of the observed behavior.')
    suggestion = models.TextField(verbose_name='My suggestion to improve or change the behavior:',
                                  help_text='Provide the feedback suggestion for improvement.')
    date = models.DateTimeField(editable=False)
    user = models.ForeignKey(User, editable=False)
    sender = models.CharField(max_length=30, null=True, blank=True, verbose_name='Yours Sincerely,',
                              help_text='Your feedback is anonymous. \
                              But you can put your name here in case you want the manager know who sent the feedback.')

    def __unicode__(self):
        return "Feedback to " + self.user.username
