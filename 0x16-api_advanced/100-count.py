#!/usr/bin/python3
"""parsing title of all hot articles"""

import json
import requests

def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {}

    if not subreddit:
        return

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0'}

    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or error querying Reddit API.")
        return

    data = response.json()
    after = data['data']['after']

    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for keyword in word_list:
            if keyword in title:
                if keyword in count_dict:
                    count_dict[keyword] += 1
                else:
                    count_dict[keyword] = 1

    if after:
        return count_words(subreddit, word_list, count_dict, after)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")
