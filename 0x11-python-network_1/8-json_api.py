#!/usr/bin/python3
"""Module"""
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
   try:
        x = argv[1][0]
    except:
        x = ""
    value = {"q": x}
    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
