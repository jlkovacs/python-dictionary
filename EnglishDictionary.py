# This is a command-line-based Interactive English Dictionary

import json
from difflib import get_close_matches


data = json.load(open("data.json"))

print("\n" + "You are using an English Dictionary")


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]  # if user entered "texas" this will check for "Texas"
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]  # coverts data to lowercase
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "No similar words found. Please double check your entry."
        else:
            return "Invalid Entry!"
    else:
        return "Word not found in the Dictionary. Please double check your entry."


while True:
    word = input("\n" + "Please enter a word: ")

    output = translate(word)

    # For multiple definitions print each one
    if type(output) == list:
        for item in output:
            print("  -- " + item)
    # Print the single definition
    else:
        print("  -- " + output)

    # Ask if user wants to enter another word
    next_w = input("\n" + "Would you like to enter another word: Enter Y if yes, or N if no: ")
    if next_w.lower() == "Y" or next_w.lower() == "y":
        continue
    else:
        print("\n" + "Thanks for using this English Dictionary!")
        break
