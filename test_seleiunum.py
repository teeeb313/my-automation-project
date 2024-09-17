import requests

# URL for JSONPlaceholder posts
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to fetch posts
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    posts = response.json()
    
    # Print the title of the first post
    first_post = posts
