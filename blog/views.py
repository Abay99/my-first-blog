from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').all()

    post = request.GET.get("post")

    if post:
        posts_list = posts_list.filter(
            Q(title__icontains=post)|
            Q(text__icontains=post)
        ).distinct( )

    paginator = Paginator(posts_list, 5)  # Show 55 posts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')











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
        before_counter = Post.objects.all().count()
        user = User.objects.create(username='tester', password='testword')
        post = Post.objects.create(author=user, title="cfcfd", text="bhjkn")
        # post_new(user)
        after_counter = Post.objects.all().count()
        self.assertNotEqual(before_counter, after_counter)

    # def test_pos_new_by_title(self):
    #     user = AnonymousUser()
    #     a = post_new(user)


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




