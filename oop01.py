#!/usr/bin/python3
"""RZFeeser | Dell / Alta3
Learning to build and work with classes"""

class Dog:
    def __init__(self, name, age):
        self.name = name   # Dog.name is now the name passed to our class
        self.age = age     # Dog.age is now the age passed to our class

    def __str__(self):
        return f"Your dog, {self.name}, is {self.age}"

    def aged(self, yearsolder):
        self.age = self.age + yearsolder

def main():
    # create a doge
    d1 = Dog("Larry", 2)
    # display the doge
    print(d1)
    # what are you?
    print(type(d1))
    # what names are within this doge
    print(dir(d1))

    # print just the age attribute
    print(d1.age)
    # print just the name attribute
    print(d1.name)

    # make larry the dog get 1 year older
    d1.aged(1)

    # larry should now be a bit older...
    print(d1)

    # list of dogs we want to keep track of
    dogsToAdopt = []

    # place first dog in our list
    dogsToAdopt.append(d1)

    # a new dog came to the shelter
    d2 = Dog("Benji", 4)

    # add the new dog to the shelter
    dogsToAdopt.append(d2)

    # show off why objects make life easier!
    print(f"The dog that has been at the shelter the longest is {dogsToAdopt[0]}. He is a goodboy, and is named {dogsToAdopt[0].name}")

if __name__ == "__main__":
    main()
