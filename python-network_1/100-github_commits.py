#!/usr/bin/python3
"""lists"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    com = req.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                comm[j].get("sha"),
                comm[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
