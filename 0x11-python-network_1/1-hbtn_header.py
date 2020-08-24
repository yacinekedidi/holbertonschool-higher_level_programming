#!/usr/bin/python3
"""Module"""
import urllib.request
import sys
argv = sys.argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
