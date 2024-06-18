import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If not a valid subreddit, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    if "data" in data and "children" in data["data"]:
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")

