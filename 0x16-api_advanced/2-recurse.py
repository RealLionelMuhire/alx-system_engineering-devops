#!/usr/bin/python3
"""returning a list containing titles of all articles"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """to ten post recursively"""

    global after
    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}

    results = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)

    if results.status_code == 200:
        afterData = results.json().get("data").get("after")

        if afterData is not None:
            after = afterData
            recurse(subreddit, hot_list)

        titles = results.json().get("data").get("children")
        for title_ in titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
