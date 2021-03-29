#!/usr/bin/python3
'''RZFeeser || RZFeeser@alta3.com
Best practice script and learning about input function'''

# constant / global (exection is it does not change)
ASTROS = "http://api.open-notify.org/astros.json"

def main():
    '''this is our runtime code'''
    # input() is a standard library function
    urianswer = input("What is the URI you would like looked up:\n")
    print(urianswer)
main()
