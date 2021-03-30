#!/usr/bin/python3


# create a function
def main():
    with open("python_made.txt", "w") as myfile:
        myfile.write("Tuesday morning\n")
        myfile.write("learning how to create files\n")


if __name__ == "__main__":
    main()
