import json

data = json.load(open("data.json"))

question = input("Input the word to search: ")

wrongWord = "There is really the word???"

possibleTypo = "The word is not found.  Maybe did you wanna say..."

def answer(question):
    try:
        print(data[question])
    except:
        return(wrongWord)

print(answer(question))

print(possibleTypo)
