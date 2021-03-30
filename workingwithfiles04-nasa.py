#!/usr/bin/python3

import requests

APOD = "https://api.nasa.gov/planetary/apod?api_key="

# open file and read out cred ~/nasa.cred
def nasacred():
    with open("/home/student/nasa.cred") as f:
        nasakey = f.read()
        nasakey = nasakey.rstrip("\n")
        return nasakey

def main():

    # grab our API key
    nasakey = nasacred()

    # make api lookup to nasa APOD
    r = requests.get(APOD + nasakey)
    
    # determine if r is a "200"
    if r.status_code != 200:
        print(r.status_code)
        print(r.json())
        exit()

    # grab JSON off our response
    r = r.json()

    # open file to write out data (append mode)
    with open("apod.data", "a") as f:
        # write out title
        f.write(r.get("title") + "\n")

        # write out date
        f.write(r.get("date") + "\n")
    
        # write out HDURL
        f.write(r.get("hdurl") + "\n")

        # two blank lines
        f.write("\n\n")

if __name__ == "__main__":
    main()
