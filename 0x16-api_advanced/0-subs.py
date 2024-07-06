#!/usr/bin/python3

"""
A module that queries a reddit api for the number of subs for a given
subreddit.
"""

import requests


BASE_URL = 'http://www.reddit.com/'


def number_of_subscribers(subreddit):
    "takes a subreddit name, returns it's subs count"

    if subreddit is None or type(subreddit) is not str:
        return 0

    api_url = 'r/' + subreddit + '/about.json'
    headers = {'User-Agent': 'getNumOfSubs by Akram'}

    r = requests.get(BASE_URL + api_url, headers=headers)

    subscribers_count = r.json().get('data', {}).get('subscribers', 0)
    return subscribers_count
