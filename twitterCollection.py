import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Bearer token from environment variables
bearer_token = os.getenv('BEARER_TOKEN')

# Formulate your query
query = "#ProgrammingParadigms @NortheasternCA"

# Construct the request URL
url = f"https://api.twitter.com/2/tweets/search/recent?query={query}"

# Set up headers with your authentication using the Bearer token from the environment variable
headers = {"Authorization": f"Bearer {bearer_token}"}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    tweets = response.json()
    # Process the tweets here
    print(tweets)
else:
    print("Request failed:", response.status_code)
    print(response.text) 
