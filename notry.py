#!/usr/bin/python3

# Start with an infinite loop
while True:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
