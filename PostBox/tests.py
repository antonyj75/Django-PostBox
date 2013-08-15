"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

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
        
