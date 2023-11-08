#!/usr/bin/bash

import requests


def number_of_subscribers(subreddit):
    """Providing a subreddit name as command-line arg
    and return subs number or 0 if the subreddits is invalid"""
    url = "https://www.reddit.com/r/{}/about.json" .format(subreddit)

    headers = {'User-Agent': 'YourAppName/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0


if __name__=='__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subs = number_of_subscribers(subreddit)
        print(subs)