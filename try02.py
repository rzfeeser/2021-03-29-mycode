#!/usr/bin/python3

# Start with an infinite loop
while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    # this ONLY traps issues with file not found
    except FileNotFoundError:
        print("Error with that file name! Try again...")
    # this prevents CTRL + C from working (not good UI design!)
    except KeyboardInterrupt:
        print("Nice try. You're stuck here... FOR-EV-VER")
