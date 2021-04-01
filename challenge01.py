#!/usr/bin/python3
"""RZFeeser || Alta3 Research
Quiz Show"""

import crayons
import json

def questions():
    with open("questions.json", "r") as qs:
        questions = json.load(qs)
    return questions

def main():
    print(f"Welcome to the {crayons.blue('Quiz Show')}")
    questions = questions()

    for question in questions:
        answer = input("What is your answer? ")
        if answer == question.get("answer"):
            print("Correct!")
        else:
            print("You lost :(")
            exit()


if __name__ == "__main__":
    main()
