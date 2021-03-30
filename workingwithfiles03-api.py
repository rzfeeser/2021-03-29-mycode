#!/usr/bin/python3

import requests

# define api we are going to interact with
ISSNOW = "http://api.open-notify.org/iss-now.json"

def main():
    # make request to that API (send HTTP GET)
    r = requests.get(ISSNOW)
    # strip json off 200 response and write into a file
    with open("iss_location", "a") as issloc:
        issloc.write("The current location of the ISS is:\n")
        issloc.write(str(r.json()))
        issloc.write("\n")

if __name__ == "__main__":
    main()
