import requests
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from posts.models import Address, Company, Post, User

USERS_URL = 'http://jsonplaceholder.typicode.com/users'
POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'


def get_json(url: str) -> list:
    r = requests.get(url)
    return r.json()


def parse_users():
    json_data = get_json(USERS_URL)

    for item in json_data:
        address = Address()
        address.city = item['address']['city']
        address.street = item['address']['street']
        address.suite = item['address']['suite']
        address.zipcode = item['address']['zipcode']
        address.lat = item['address']['geo']['lat']
        address.lng = item['address']['geo']['lng']

        try:
            address.save()
        except IntegrityError:
            address = Address.objects.filter(
                city=item['address']['city'],
                street=item['address']['street'],
                suite=item['address']['suite'],
            ).first()

        company = Company()
        company.name = item['company']['name']
        company.catchphrase = item['company']['catchPhrase']
        company.bs = item['company']['bs']

        try:
            company.save()
        except IntegrityError:
            company = Company.objects.filter(name=item['name']).first()

        try:
            user = User()
            user.name = item['name']
            user.username = item['username']
            user.email = item['email']
            user.phone = item['phone']
            user.website = item['website']
            user.address = address
            user.company = company
            user.save()
        except IntegrityError:
            pass


def parse_posts():
    json_data = get_json(POSTS_URL)

    for item in json_data:
        try:
            post = Post()
            post.id = item['id']
            post.title = item['title']
            post.body = item['body']
            post.user = User.objects.get(pk=item['userId'])
            post.save()
        except ObjectDoesNotExist:
            pass


def load_data():
    parse_users()
    parse_posts()


def delete_data():
    User.objects.all().delete()
    Address.objects.all().delete()
    Company.objects.all().delete()


def get_posts():
    posts = Post.objects.values('user__name', 'title', 'body')
    return posts
