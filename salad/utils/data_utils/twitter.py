# -*- coding: utf-8 -*-
from urllib.parse import quote

from requests_oauthlib import OAuth1Session

from salad.config import (
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET,
)
from salad.utils.class_utils import Singleton


class Twitter(metaclass=Singleton):
    def __init__(self):
        self.api = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    def get_tweets(self):
        response = self.api.get('https://api.twitter.com/1.1/search/tweets.json', params=dict(
            q=quote('from:hatebu ntt'),
            # lang='ja',
            count=100,
        )).json()
        for status in response['statuses']:
            if '退' in status['text']:
                yield status
