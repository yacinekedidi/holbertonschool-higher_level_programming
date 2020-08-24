#!/usr/bin/python3
"""Module"""
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    c = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(c[i].get("sha"), 
                                  c[i].get("commit").get("author").get("name")))
    except:
        pass
