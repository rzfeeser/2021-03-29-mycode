#!/usr/bin/python3
"""RZFeeser || Python Review
Reviewing how to use requets library"""

# we want to perform an API lookup to NASA
import requests

# if we want to make the txt on the screen be colorful
import crayons

# define our API to lookup
API = "https://api.nasa.gov/DONKI/CME?startDate=2017-01-03&endDate=2017-01-03&api_key=DEMO_KEY"


def main():
    # make the API request
    sflare = requests.get(API)

    # make sure we got back a 200 response
    if sflare.status_code != 200:
        print(f"Uh oh, something is wrong with the API. We returned a {sflare.status_code}")
        exit()

    # strip of JSON if we did get back 200 response
    sflare = sflare.json()

    # grab data from JSON that we want to loop through
    #print(sflare[0].get("cmeAnalyses")[0].get("enlilList")[0].get("impactList"))
    sfevents = sflare[0].get("cmeAnalyses")[0].get("enlilList")[0].get("impactList")

    # looping through the data that describes impeding doom
    for sfevent in sfevents:
        if sfevent.get("location").lower() == "earth":
            print(f"{crayons.yellow('Put on SPF 10,000')}")
        else:
            print("Safe another day!")

    # IF location is marked for EARTH print to the screen
    # use a color to make it "pop"

if __name__ == "__main__":
    main()
