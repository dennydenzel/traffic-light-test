from posts.models import Post, User
from django.forms import ModelForm
from posts.forms import PostForm
import json
import requests


USERS_URL = 'http://jsonplaceholder.typicode.com/users'
POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'


def get_json(url: str) -> list:
    r = requests.get(url)
    return r.json()


def parse_posts_json() -> list:
    posts_json = get_json(POSTS_URL)
    posts = []

    for item in posts_json:
        post = {
            'id': item.get('id'),
            'title': item.get('title'),
            'body': item.get('body'),
            'user': item.get('userId'),
        }
        posts.append(post)
    return posts


def create_objects(function, ModelForm: ModelForm) -> list:
    list_data = function()
    objects = []

    for item in list_data:
        form = ModelForm(data=item)
        if form.is_valid():
            object = form.save(commit=False)
            objects.append(object)
    print(objects)
    return objects


def load_posts():
    post_objects = create_objects(parse_posts_json, PostForm)
    Post.objects.bulk_create(post_objects)
    print(Post.objects.all())


def get_posts():
    print(Post.objects.all())
    return Post.objects.all()
