import os
import json

while True:
    if os.path.exists("data.json"):
        data = json.load(open("data.json"))
        print("Enter a word ... ")
        word = input()   
        print(data[word])     
    else:
        print("source not found.")
 