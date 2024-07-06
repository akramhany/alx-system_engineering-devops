#!/usr/bin/python3

"""
A module that queries a reddit api for the number of subs for a given
subreddit.
"""

import requests


BASE_URL = 'https://www.reddit.com/'


def get_mod_hashes():
    "returns the mod_hashes of reddit api"

    r = requests.get(BASE_URL + '/api/me.json')

    return r.json()


def number_of_subscribers(subreddit):
    "takes a subreddit name, returns it's subs count"

    api_url = 'r/' + subreddit + '/about.json'
    headers = {'User-Agent': 'getNumOfSubs by Akram',
               'Accept': 'application/json'}

    r = requests.get(BASE_URL + api_url, headers=headers)

    try:
        subscribers_count = r.json()['data']['subscribers']
    except Exception:
        subscribers_count = 0

    return subscribers_count
