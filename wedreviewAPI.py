#!/usr/bin/python3
"""RZFeeser || exploring a catfact api
we ran this example in jenkins"""

CATFACT = "https://cat-fact.herokuapp.com/facts"

# make HTTP requests
import requests

def main():
    """runtime function"""
    # make request call to URI (scheme://authority/path/to/service)
    r = requests.get(CATFACT)

    # strip JSON off of (assumed 200) response (r)
    catfacts = r.json()

    # open file to write to
    with open("catfacts.txt", "w") as cf:
        # write a simple header into our data
        print(f"Some cat facts from {CATFACT}", file=cf)
        # loop through data
        for catfact in catfacts:
            #cf.write(f"{catfact.get('text')}\n")
            #cf.write(catfact.get('text') + "\n")
            print(catfact.get('text'), file=cf)

if __name__ == "__main__":
    main()
