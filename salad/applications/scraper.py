# -*- coding: utf-8 -*-
from urllib.request import urlopen

from bs4 import BeautifulSoup

from salad import logger


def fetch_entries_v1():
    html = urlopen('http://b.hatena.ne.jp/entrylist/all/NTT').read()
    soup = BeautifulSoup(html, features='html.parser')
    for node in soup.find_all('a', attrs={'data-gtm-click-label': 'entry-info-title'}):
        yield node


def fetch_entries_v2():
    html = urlopen('https://twitter.com/search?q=from%3Ahatebu%20ntt&src=typd').read()
    soup = BeautifulSoup(html, features='html.parser')
    logger.info(soup)
    for node in soup.find_all('div', class_='content'):
        x = node.find('p', class_='tweet-text')
        logger.info(x)

    # for node in soup.find('ol', id='stream-items-id').find_all('img', class_='u-block'):
        # logger.info(node)


def download_entities():
    pass


if __name__ == '__main__':
    # x = fetch_entries_v1()
    # logger.info(x)
    fetch_entries_v2()
