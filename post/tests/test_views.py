from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from ..models import Post
from taggit.models import Tag


class SetQueryTestCase(TestCase):

    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            username='test_user',
            email='test_email@example.com',
            password='tesutopasuwa-do',
        )

        self.post = Post.objects.create(
            user=self.test_user,
            title='test_title',
            content='This is a test content.',
        )

        test_tags = ['test_tag1', 'test_tag2', 'test_tag3']
        for tag in test_tags:
            self.tag = Tag.objects.create(name=tag)
            self.post.tags.add(self.tag)


class TestIndexView(SetQueryTestCase):

    def test_get(self):
        response = self.client.get(reverse('post:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: {}>'.format(self.post.title)])
        self.assertContains(response, self.post.title)

    def test_tag_get(self):
        response = self.client.get(reverse('post:index_tag', kwargs={'tag': 'test_tag1'}))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: {}>'.format(self.post.title)])
        self.assertContains(response, self.post.title)

    def test_search_get(self):
        response = self.client.get(reverse('post:index'), {'key_word': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: {}>'.format(self.post.title)])
        self.assertContains(response, self.post.title)

    def test_trend_get(self):
        response = self.client.get(reverse('post:index_trend'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: {}>'.format(self.post.title)])
        self.assertContains(response, self.post.title)


class TestDetailView(SetQueryTestCase):

    def test_get(self):
        response = self.client.get(reverse('post:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)

    def test_not_get(self):
        response = self.client.get(reverse('post:post_detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, 404)


class TestInquiryView(SetQueryTestCase):

    def test_get(self):
        response = self.client.get(reverse('post:inquiry'))
        self.assertEqual(response.status_code, 200)

    def test_post_success(self):
        params = {
            'name': 'test_user',
            'email': 'test_inquiry_email@example.com',
            'title': 'test_title',
            'message': 'This is a test message.'
        }

        response = self.client.post(reverse('post:inquiry'), params)
        self.assertRedirects(response, reverse_lazy('post:inquiry'))

    def test_post_failure(self):
        response = self.client.post(reverse('post:inquiry'), params={})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'errorlist')


class TestCommonTemplateView(TestCase):

    def test_privacy_get(self):
        response = self.client.get(reverse('post:privacy'))
        self.assertEqual(response.status_code, 200)

    def test_profile_get(self):
        response = self.client.get(reverse('post:profile'))
        self.assertEqual(response.status_code, 200)
