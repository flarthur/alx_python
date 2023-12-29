"""
GitHub API user-id-retriever

This script retrieves the user ID from the GitHub API 

args:
    username(str): GitHub username.
    password(str): GitHub password.

Returns:
    int: user's GitHub ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_obj = response.json()
    print(json_obj.get("id"))
