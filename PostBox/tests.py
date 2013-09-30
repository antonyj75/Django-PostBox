"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from PostBox.models import Feedback

class PostBoxViewTests(TestCase):
    def test_welcome_message(self):
        """
        As a visitor to the site, I should see the welcome message,
        so that I know I am on the right page.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Feedback Postal Service", 1, response.status_code)

    def test_posttype_selection(self):
        """
        As an ignorant user, when I press Submit without making a selection,
        then I should see error message and should be on the same page.
        """
        response = self.client.get('/selection/')
        self.assertContains(response, 'Please select what you want to post')

    def test_feedbackpage_display(self):
        """
        Given a team member id, I should see the feedback page.
        """
        user1 = User.objects.create(username='Test', password='password')
        response = self.client.get(reverse('PostBox:feedback', args = (user1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Feedback post to <cite>Test')

    def test_feedback_entry_without_giving_sender(self):
        """
        As a feedback giver, I should be able to provide feedback anonymously.
        """
        user1 = User.objects.create(username='Test', password='password')
        response = self.client.post(reverse('PostBox:feedback', args = (user1.id,)),
            {'suggestion': 'Smile Well'})
        # When we post with only the suggestion and omitting all other fields including sender,
        # the app should save the data and redirect to the success page.
        # The following assert tests only the redirection.
        # I don't know how to ensure that the redirected page is success page.
        self.assertEqual(response.status_code, 302)


class PostBoxModelTests(TestCase):
    def test_feedback_entry(self):
        """
        Verify that when a feedback is submitted, it is associated with the intended user.
        """
        feedbackRecipient = User.objects.create(username='Test', password='password')
        feedbackEntry = Feedback.objects.create(example='You did not post code for review',
                                                consequence='This may lead to bad code',
                                                suggestion='Please post code for review',
                                                user=feedbackRecipient, date=timezone.now())
        feedbackRead = Feedback.objects.get(user_id=feedbackRecipient.id)
        self.assertEqual(feedbackEntry.example, feedbackRead.example)
