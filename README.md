# NYT Letter Boxed Solver

## Overview
LetterBoxedSolver is a Python program that identifies optimal solutions to the popular NYT game Letter Boxed.

## Details
The program uses the Argeparse library to define command-line flags that allow you to specify various options.
You can either provide your own puzzle in the format abc-def-ghi-jkl or fetch the current puzzle directly from the NYT website.
It does this by using the BeautifulSoup library to web scrape metadata that includes the sides of the puzzle along with a list of valid words for that day's puzzle.
You can also specify the maximum word length for a solution to be printed. The default max solution length is 3, but using a max length of 2 gives you the most optimal solution for the puzzles.
Due to the high time complexity of the puzzle, I would not recommend using a max length greater than 3. Depending on the puzzle, a max length of just 4 can cause the program to run for up to 10 minutes.

When solving the current day's puzzle, the program can use a relatively small dictionary of only the valid words for that day (scraped from the NYT website).
When solving a different puzzle, however, the program must begin with a larger dictionary of words and then choose only the words that are valid for that specific puzzle.
This presents a challenge because LetterBoxed allows many words that are proper nouns, names, or slang terms which are not included in dictionaries.
In order to account for these words that would be missed by a typical word list, I began saving the valid words from each day and combining them with a preexisting word list.
I did this by scheduling a script to run every night after the new day's puzzle is uploaded using MacOS Launchd script management.
The script fetches the valid words, adds them to a list, and then commits the changes to this repository.
