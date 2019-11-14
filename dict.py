import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json", "r"))

def translate(w):
    w = w.lower()
    if w in data:
        meaning = data[w]
        return meaning
    elif len(get_close_matches(w , data.keys())) >= 1 :
        w = get_close_matches(w , data.keys())[0]
        yon = input( "Do You mean " + get_close_matches(w , data.keys())[0] + ". If Yes press Y If No press N!")
        yon = yon.lower()
        if yon == "y":
            meaning = data[w]
            return meaning
        elif yon == "n":
            return "You entered the Wrong Word. Please double check it!"
        else:
            return "You entered the Wrong Word. Please double check it!"

    else:
        return "You entered the Wrong Word. Please double check it!"


while True:
    word = input("Enter Word: ")
    meaning = translate(word)

    if type(meaning) == list:
        for i in meaning:
            print(i)
    else:
        print(meaning)
