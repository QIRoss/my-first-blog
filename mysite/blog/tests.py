from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from .forms import PostForm
from django.utils import timezone

class PostModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test post
        self.post = Post.objects.create(
            author=self.user,
            title='Test Title',
            text='Test Text',
            created_date=timezone.now()
        )

    def test_post_model(self):
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.title, 'Test Title')
        self.assertEqual(post.text, 'Test Text')

    def test_post_form(self):
        data = {
            'author': self.user.id,  # You may need to update this depending on your User model
            'title': 'New Title',
            'text': 'New Text',
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_publish_method(self):
        post = Post.objects.get(id=self.post.id)

        print(repr(post))
        post.publish()
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.published_date.date(), timezone.now().date())
        self.assertIsNotNone(post.published_date)
