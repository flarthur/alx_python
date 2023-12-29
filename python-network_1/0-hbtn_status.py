"""Fetch https://alx-intranet.hbtn.io/status status
"""
import requests

if __name__ == "__main__":
    """
    Fetches the status of https://alx-intranet.hbtn.io/status and prints details.

    Output:
        - Body response:
            - type: <class 'str'> (type of response content)
            - content: <response content>
    """

    url = "https://alx-intranet.hbtn.io/status"
    result = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))
