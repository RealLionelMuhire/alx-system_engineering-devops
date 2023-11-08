#!/usr/bin/python3
"""
1-main
"""
import requests
import sys


def top_ten(subreddit_name):
    """Prints the titles of the top 10 posts in a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit_name}/hot.json?limit=10"

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
                print("No posts found.")
        elif response.status_code == 404:
            print("None")
        else:
            print("API error.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
