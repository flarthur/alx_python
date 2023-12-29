"""
Simple http request Script Documentation
"""

import sys
import requests


if __name__ == "__main__":
    """
    Main script to make an HTTP GET request and display the response body.

    """
    url = sys.argv[1]
    response = requests.get(url)
    body = response.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(body)
