"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

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
