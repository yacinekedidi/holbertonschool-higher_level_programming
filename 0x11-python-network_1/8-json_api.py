#!/usr/bin/python3
"""Module"""
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
   try:
        x = argv[1]
    except:
        x = ""
    value = {"q": x}
    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    if r.json():
        print("[{}] {}".format(r.json().get("id"), r.json().get("name")))
    else:
        print("No result")
