import json
import sys
from difflib import SequenceMatcher
from difflib import get_close_matches  #using this as it has a return max paramter(instead of if loop printing all)

data = json.load(open("data_file.json","r"))

def findWord():
    print("Welcome to Command Line Dictionary!")
    print("Type exit() to escape")
    word = input("Enter a word...\n")
    word.lower()
    if word in data:
        return data[word]
    else:
        print("sorry word not found")
        print("Did you mean any of these words?")
        return similarWord(word)
        

def similarWord(word):

    alternitives = get_close_matches(word,data.keys(), n = 5)
        # if s.quick_ratio() > 0.75:
        # alternitives.append(words)
    return alternitives

print(findWord())