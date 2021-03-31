#!/usr/bin/python3

import requests

JENKINSAPI = "http://0.0.0.0:2224/api/json"


# make a request to Jenkins for dashboard info
# pass in un and token (read this in from a file)
def grabcreds():
    # open a file in /home/student with UN / API token
    with open("/home/student/jenkins.creds", "r") as jc:
        creds = jc.readlines()
        return creds # list or tuple

def main():
    # call grabcreds
    creds = grabcreds()
    # make request to JENKINSAPI
    r = requests.get(JENKINSAPI, auth=(creds[0].rstrip("\n"), creds[1].rstrip("\n")))

    # print the dashboard information to the screen as YAML
    print(r.json())


if __name__ == "__main__":
    main()
