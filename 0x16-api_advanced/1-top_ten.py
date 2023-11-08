#!/usr/bin/python3
"""printing ton 10 subs"""

import requests

def top_ten(subreddit_name):
    """top ten printer"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit_name)

    headers = {'User-Agent': 'YourAppName/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    print(post['data']['title'])
                else:
                    print("No post found.")
            elif response.status_code == 404:
                print("None")
            else:
                print("API error.")
    except requests.exceptions.RequestExecption as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
