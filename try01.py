#!/usr/bin/python3

# Start with an infinite loop
while True:
    try:
        name = input("Enter a filename: ")
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again...")
