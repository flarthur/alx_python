"""
Simple User Search Script

This script performs a user search using an API.
"""

import sys
import requests


if __name__ == "__main__":
    """API URL for user search"""
    url = "http://0.0.0.0:5000/search_user"
    """Get search query from command-line argument"""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    """Prepare query payload"""
    payload = {"q": q}
    """Send POST request to API"""
    response = requests.post(url, data=payload)
    """Try to parse JSON response"""
    try:
        json_outp = response.json()

        """Check if there are search results"""
        if not json_outp:
            print("No result")
        else:
            """Extract user ID and name from response"""
            my_id = json_outp.get("id")
            my_name = json_outp.get("name")
            """Display user information"""
            print("[{}] {}".format(my_id, my_name))
    except ValueError as invalid_json:
        """Handle invalid JSON response"""
        print("Not a valid JSON")
