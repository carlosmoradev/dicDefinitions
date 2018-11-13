import json

data = json.load(open("data.json"))

question = input("Input the word to search: ")

print(data[question])
