#!/usr/bin/python3

"""SENDS A POST"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    dta = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, dta)
    with urllib.request.urlopen(req) as ans:
        print(ans.read().decode("utf-8"))
