import json

data = json.load(open("data.json"))

question = input("Input the word to search: ")

def answer(question):
    try:
        print(data[question])
    except:
        print("There is a really word???")

print(answer(question))
