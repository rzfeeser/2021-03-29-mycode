#!/usr/bin/python3

def main():

    fileloc = input("Where is the file to open? ")

    with open(fileloc, "a") as myfile:
        myfile.write("We added this line to the bottom of the file\n")

    # old way of opening a file (you'll still see this)
    myfile = open(fileloc, "r")
    # print out the entire contents of the file (.read() reads all data as a single string)
    print(myfile.read(), end="")
    # because we opened the file using an old method, we need to manually close it (best practice)
    myfile.close()



if __name__ == "__main__":
    main()
