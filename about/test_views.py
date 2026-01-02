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
