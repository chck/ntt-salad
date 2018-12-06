# -*- coding: utf-8 -*-
import pytest

from salad.utils.data_utils.twitter import Twitter
from salad import logger


def test_get_tweets():
    tweets = [tweet for tweet in Twitter().get_tweets()]
    logger.info(len(tweets))
    assert True == False
    assert 0 != len(tweets)


if __name__ == '__main__':
    pytest.main([__file__])
