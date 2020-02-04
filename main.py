import json
import sys
from difflib import SequenceMatcher
from difflib import get_close_matches  #using this as it has a return max paramter(instead of if loop printing all)

data = json.load(open("data_file.json","r"))

def findWord():
    print("Welcome to Command Line Dictionary!")
    print("Type exit() to escape")
    while True:
        word = input("ENTER A WORD...\n")
        if word in data:
            for item in data[word]:
                print(item)       #check for Proper nouns before coverting to lower
            continue
        word = word.lower()
        if word == "exit()":
            sys.exit()
        if word in data:
            for item in data[word]:
                print(item)
        else:
            lst = similarWord(word)
            if len(lst) == 0:
                 print("Sorry, no similar words found. Please double check it.")
            else:
                print("Could not find word")
                print("Enter Yes or No to the following questions")
                for i in range(len(lst)):
                    choice = input("Did you mean %s?\n" % lst[i])
                    if 'y' in choice.lower():
                        for item in data[lst[i]]:
                            print(item)
                        break
                    elif i == len(lst) - 1:
                        print("This word doesn't seem to exist, try again!")
                    



def similarWord(word):
    alternitives = get_close_matches(word,data.keys(), n = 5, cutoff = 0.7)
        # if s.quick_ratio() > 0.75:
        # alternitives.append(words)
    return alternitives




findWord()