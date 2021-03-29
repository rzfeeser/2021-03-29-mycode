#!/usr/bin/python3
"""Learning to do API lookups"""

import requests

def main():
    # This will send an HTTP GET to the URI
    # this EXPECTS a 200 response
    astros = requests.get("http://api.open-notify.org/astros.json")

    # json() is a METHOD avail to astros HTTP requests object
    astrodata = astros.json()

    print(astrodata)

    print(astrodata.get("people"))

    print(astrodata.get("people")[1])

    print(astrodata.get("people")[1].get("name"))

main()
