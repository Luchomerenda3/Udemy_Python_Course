import json
import difflib as dl


#Define the funciton to return the available meanings in the dictionary for a certain word:

def meaning(dictionary,word):

    if word.lower() in dictionary.keys():
        return word.capitalize(), dictionary[word]
    if word.upper() in dictionary.keys():
        return word.upper(), dictionary[word.upper()]
    elif word.capitalize() in dictionary.keys():
        return word.capitalize(),dictionary[word.capitalize()]
    elif len(dl.get_close_matches(word,dictionary.keys())) > 0:
        word = input(f"Did you mean any of these words {dl.get_close_matches(word,dictionary.keys())}?\nIf yes enter word again, if No enter N: ")
        if word != "N":
            return word.capitalize(),dictionary[word]
        else:
            print("Searched word couldn't be found, please check again.")
            return word.capitalize(),None
    else:
        print("Searched word couldn't be found, please check again.")
        return word.capitalize(),None

#Lets import the data
with open("data.json","r") as data:
    dict = json.load(data)

print("Welcome to the python dictinoary V1.2")
#lets ask the user what they need

user_search = input("Please enter which word are you looking for: ")
while user_search != "ss":

    search = meaning(dict,user_search)
    if search[1] != None:
        print(f"{search[0]}: ")
        for i in range(0,len(search[1])):
            print(f"{len(search[0])*' '}{search[1][i]}")

    print("\nIf you want to stop searching please enter \"ss\"")
    user_search = input("Else enter your next search word: ")


print("Thanks for using python dictionary V1.0")