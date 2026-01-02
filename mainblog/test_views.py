from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post


class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        """Test that the post detail page renders correctly with comment form.
        view returns different things depending on if the request method used is GET or POST. To access the response that our view would return to a GET request, the self.client.get() method is used, with the reverse method passed in to generate the relevant URL with the provided view arguments.
        b"". This syntax is for creating byte strings, which is crucial because all internet data, including the HTTP response content in response.content, is in byte format. This differs from Python's standard use of Unicode strings.
        """
       # print(response.context)
        # Confirms that the view responds successfully, a fundamental check for any web page.
        self.assertEqual(response.status_code, 200)
        # ensure that the content we defined for self.post in setUp (the blog title and content) will be rendered as part of the response, verifying that our view correctly displays the blog post.
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        """
        ensure that the content we defined for self.post in setUp (the blog title and content) will be rendered as part of the response, verifying that our view correctly displays the blog post.
        """
        self.assertIsInstance(
            # checks that the correct form is being used in the context.
            response.context['comment_form'], CommentForm)
