#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    if after:
        url += f'&after={after}'
    
    headers = {'User-Agent': 'YourAppName/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                if not posts:
                    return print_counts(counts)
                
                for post in posts:
                    title = post['data']['title'].lower()
                    for word in word_list:
                        word = word.lower()
                        if word not in counts:
                            counts[word] = 0
                        counts[word] += title.count(f' {word} ')
                
                next_page = data['data']['after']
                return count_words(subreddit, word_list, next_page, counts)
            else:
                return print_counts(counts)
        elif response.status_code == 404:
            return print_counts(counts)
        else:
            return print_counts(counts)
    except requests.exceptions.RequestException:
        return print_counts(counts)

def print_counts(counts):
    # Sort counts by value (count) in descending order, and then alphabetically
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
