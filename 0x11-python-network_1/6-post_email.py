#!/usr/bin/python3
"""Module"""
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
