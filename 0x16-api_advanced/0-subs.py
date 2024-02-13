import json
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers 
    """
    url ="https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)

    reddit = response.json()

    try:
        total_subscribers = reddit.get('data').get('subscribers')
        return int(total_subscribers)
    except:
        return 0