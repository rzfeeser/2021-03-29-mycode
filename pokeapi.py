#!/usr/bin/python3
"""rzfeeser || alta3 research
experimenting with api lookups and writing out data returned via HTTP + json"""

# gobal / constant defining where pokeAPI service is
POKEAPI = "https://pokeapi.co/api/v2/pokemon/"

# python3 -m pip install requests
# this is used for looking up APIs (URL content / HTTP requests)
import requests


def pokedex(pokedata):
    with open("pokedex", "a") as pd:
        pd.write(str(pokedata))
    return True

# performs the HTTP API lookup
def lookuppm(pokename):
    # attempt to lookup pokemon by name
    r = requests.get(POKEAPI + pokename)
    # if a 200 is returned...
    if r.status_code == 200:
        # strip off the JSON and return it!
        return r.json()
    # if you didn't get back a 200, it failed, return NONE
    else:
        return None


def main():
    
    # print out to the screen
    print("Welcome to the PokeAPI Client")

    # collect input assign to "pokename" (this is the pokemon to lookup)
    pokename = input("What Pokemon would you like to attempt to capture? ")
    
    # call lookuppm function
    pokedata = lookuppm(pokename)

    # if we were able to get back data
    if pokedata:
        print(f"Suddenly, a wild {pokename} appears!")
        
        save = input("Save this one to the pokedex? ")
        # does user want to save the pokemon data that was returned
        if save.lower() == "y" or save.lower() == "yes":
            pokedex(pokedata)
            # successful
            print(f"{pokename} saved!")
        else:
            # user did not want to save the data
            print(f"{pokename} has escaped!")

    else:
        # the lookup failed to return any relevant data
        print(f"You spent all day looking for a {pokename} and can't find it.")

if __name__ == "__main__":
    main()
