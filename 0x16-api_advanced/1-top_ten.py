#!/usr/bin/python3

"""A module that solves the top ten task for alx api"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hottest posts liked for a
    given subreddit"""

    r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     headers={'User-Agent': 'Myscript for 10 hottest posts'},
                     params={'limit': 10})

    if r.status_code == 404:
        print('None')
        return

    for res in r.history:
        if res.status_code == 404:
            print('None')
            return

    posts = r.json().get('data', {}).get('children', [])

    if not posts:
        print('None')

    for post in posts:
        print(post.get('data', {}).get('title'))
