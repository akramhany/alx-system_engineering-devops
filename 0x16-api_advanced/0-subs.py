#!/usr/bin/python3

"""
A module that queries a reddit api for the number of subs for a given
subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    "takes a subreddit name, returns it's subs count"

    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {'User-Agent': 'getNumOfSubs by Akram'}

    r = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=headers)

    subscribers_count = r.json().get('data', {}).get('subscribers', 0)
    print('OK')
    return subscribers_count
