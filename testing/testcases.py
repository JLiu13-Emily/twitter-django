from django.test import TestCase as DjangoTestCase
from django.contrib.auth.models import User
from tweets.models import Tweet

class TestCase(DjangoTestCase):
    def create_user(self, username, email=None, password=None):
        if password is None:
            password = 'generic password'
        if email is None:
            email = f'{username}@twitter.com'
        #不能写成 USer.objects.create()
        #因为 password需要被加密，username和email需要进行一些normalize
        return User.objects.create_user(username, email, password)
    def create_tweet(self, user, content=None):
        if content is None:
            content = 'default tweet content'
        return Tweet.objects.create(user=user, content=content)