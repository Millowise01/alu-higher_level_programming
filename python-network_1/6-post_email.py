#!/usr/bin/python3
"""Displays the header"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    req = requests.post(url, data=val)
    print(req.text)
