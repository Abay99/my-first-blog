from django.test import TestCase
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .views import *
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import AnonymousUser

from django.test import TestCase

class ViewsTestCase(TestCase):
    def setUp(self):
        me = User.objects.create(username="abaytest", password="abay")
        Post.objects.create(author=me, title="1-st tested title", text="1-st tested text")
        Post.objects.create(author=me, title="2-nd tested title", text="2-nd tested text")

    def test_post_delete(self):
        before_counter = Post.objects.all()
        post = Post.objects.get(title="1-st tested title")
        user = AnonymousUser()
        post_delete(user, post.pk)
        after_counter = Post.objects.all()
        self.assertNotEqual(before_counter, after_counter)

    def test_post_new(self):
        before_counter = Post.objects.all()
        user = User.objects.create(username='tester', password='testword')
        after_counter = Post.objects.all()
        self.assertNotEqual(before_counter, after_counter)


    # def test_exactly_that_item_deleted(self):
    #     post = Post.objects.get(title="2-nd tested title")
    #     user = AnonymousUser()
    #     post_delete(user, post.pk)
    #     post_check = Post.objects.get(post.pk)



    # def test_user_valid(self):
    #
    #     # me = User(data={'username': "abaytest", 'password': "abay"})
    #     me = User.objects.create(username="abaytest", password="abay")
    #     # form = User(username="abaytest", password="abay")
    #     self.assertTrue(me.is_active)
    #
    # def test_post_detail(self):
    #     me = User.objects.create(username="abaytest1", password="abay1")
    #     Post.objects.create(author=me, title="1-st tested title", text="1-st tested text")
    #
    #     # create Post object
    #     # ensure that it is created Post.objects.all().count == 1
    #
    #     # get url from the blog detail, use resolves('url_name') which returns path (url pattern)
    #     # do GET request self.client.get('/blog/') => response = self.client.get(URL, args=..)
    #     # assert response is html (content type)
    #     # self.assertIn(post.title, response.data.text)
    #
    #     pass




