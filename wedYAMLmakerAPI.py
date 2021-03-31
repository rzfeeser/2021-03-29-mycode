#!/usr/bin/python3
"""RZFeeser || exploring a catfact api
In this example, we convert JSON to YAML and write it out into a file.

YAML spec:
https://yaml.org/spec/1.2/spec.html
"""

CATFACT = "https://cat-fact.herokuapp.com/facts"

# import pyyaml
# yes, it is called pyyaml on pypi, but you still import yaml :(
import yaml

# make HTTP requests
import requests

def main():
    """runtime function"""
    # make request call to URI (scheme://authority/path/to/service)
    r = requests.get(CATFACT)

    # strip JSON off of (assumed 200) response (r)
    catfacts = r.json()

    # open file to write to (YAML format typically has *.yml or *.yaml)
    with open("catfacts.yaml", "w") as cf:
        # write a simple header into our data
        print(f"Some cat facts from {CATFACT}\n", file=cf)
        print(yaml.dump(catfacts), file=cf)

if __name__ == "__main__":
    main()
