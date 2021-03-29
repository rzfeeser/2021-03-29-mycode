#!/usr/bin/python3

mylist = [1,2,3]

otherlist = [4,5,6]

footrace1 = ["larry", "kevin"]

footrace2 = ["shelia", "carrie"]



# combining two lists together!
mylist.extend(otherlist)
print(mylist)

# append opens up a SINGLE slot
footrace1.append(footrace2)
print(footrace1)

#
print(mylist + otherlist)
