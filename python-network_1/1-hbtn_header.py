"""
Script to Fetch and Display a Variable from a URL's Response Header
"""
import requests
import sys

if __name__ == "__main__":
    """
    Entry point of the script.
    Fetches a variable from the response header of the specified URL.
    """
    url = sys.argv[1]
    response = requests.get(url)
    result = response.headers.get("X-Request-Id")
    print(result)
