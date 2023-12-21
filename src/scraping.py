import requests
from bs4 import BeautifulSoup

letter_boxed = requests.get("https://www.nytimes.com/puzzles/letter-boxed")
soup = BeautifulSoup(letter_boxed.text, "html.parser")

script = soup.find(lambda script: "dictionary" in script.text).text

letters = ""
for letter in script[script.find("sides")+8:]:
    if letter.isalpha():
        letters += letter.lower()
    elif letter == ",":
        letters += "-"
    elif letter == "]":
        break

todays_words = []
word = ""
for letter in script[script.find("dictionary")+13:]:
    word += letter if letter.isalpha() else ""
    if letter == ',':
        todays_words.append(word.lower())
        word = ""
    elif letter == ']':
        todays_words.append(word.lower())
        break
