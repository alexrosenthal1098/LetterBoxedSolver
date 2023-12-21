import scraping
import bisect
import os
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

sorted_words = []
with open("lb_words.txt", "r") as lb:
    for word in lb.readlines():
        sorted_words.append(word.strip())

for new_word in scraping.todays_words:
    index = bisect.bisect_left(sorted_words, new_word)
    if index == len(sorted_words) or sorted_words[index] != new_word:
        sorted_words.insert(index, new_word)

with open("lb_words.txt", "w") as lb:
    for word in sorted_words:
        lb.write(word + "\n")

applescript = f'display notification "Successfully collected today\'s letter boxed words" with title "Letter Boxed"'
subprocess.run(["osascript", "-e", applescript])
