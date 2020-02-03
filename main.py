import json
from difflib import SequenceMatcher

data = json.load(open("data_file.json","r"))

def findWord():
    word = input("Enter a word...\n")
    word.lower()
    if word in data:
        return data[word]
    else:
        print("sorry word not found")
        print("Did you mean any of these words?")
        return similarWord(word)
        

def similarWord(word):
    alternitives = []
    for words in data:
        s = SequenceMatcher(None,word,words)
        if s.quick_ratio() > 0.75:
            alternitives.append(words)
    return alternitives

print(findWord())