from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About, CollaborateRequest


class TestAboutViews(TestCase):
    def setUp(self):
        self.about = About(
            title="About Me", content="This is the about me section.")
        self.about.save()

    def test_render_about_page(self):
        response = self.client.get(reverse('about'))
        """Test that the about me page renders correctly with about information."""
        # Confirms that the view responds successfully, a fundamental check for any web page.
        self.assertEqual(response.status_code, 200)
        # ensure that the content we defined for self.about in setUp (the about title and content) will be rendered as part of the response, verifying that our view correctly displays the about section.
        self.assertIn(b"About Me", response.content)

        """
        ensure that the content we defined for self.about in setUp (the about title and content) will be rendered as part of the response, verifying that our view correctly displays the about section.
        """
        self.assertIsInstance(
            # checks that the correct about instance is being used in the context.
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        form_data = {
            'name': 'Test User',
            'email': 'test@email.com',
            'message': 'This is a test collaboration request.'
        }
        response = self.client.post(reverse('about'), form_data)
        self.assertEqual(response.status_code, 200)
        # Verify that the collaboration request was created in the database.
        self.assertTrue(CollaborateRequest.objects.filter(
            email=form_data['email'], message=form_data['message']).exists())

    """ self.assertIn( b'Collaboration request received! I endeavour to respond within 2 working days.', response.context) """
