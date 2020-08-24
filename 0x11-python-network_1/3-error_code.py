#!/usr/bin/python3
"""Module"""
from urllib import request, error
import sys
argv = sys.argv


if __name__ == "__main__":
	req = request.Request(argv[1])
	try:
    	with request.urlopen(req) as response:
        	print(response.read().decode("utf-8"))
    except error.HTTPError as e:
    	print("Error code: {}".format(e.code))
