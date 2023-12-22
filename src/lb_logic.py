import scraping


class LetterBoxed:
    def __init__(self, sides: str, dictionary: list[str]):
        # sides is a string is given in the format "abc-def-ghi-jkl"
        # self.sides is a set of strings containing the 3 letters of that side
        self.sides = {side for side in sides.split("-")}
        self.words = []
        for word in dictionary:
            if self.is_valid_word(word):
                self.words.append(word)


    def _get_side(self, letter: str, last_side: str = "") -> str:
        for side in self.sides - {last_side}:
            if letter in side:
                return side
        return ""

    def is_valid_word(self, word: str) -> bool:
        last_side = self._get_side(word[0])
        if not last_side:
            return False

        for letter in word[1:]:
            last_side = self._get_side(letter, last_side)
            if not last_side:
                return False
        return True

    def _has_new_letters(self, word: str, new_letters: set[str]):
        for letter in word:
            if letter in new_letters:
                return True
        return False

    def _add_solutions_with_words(self, words: list[str], letters_remaining: set[str], max_len: int,
                                   solutions: list[list[str]]):
        if len(letters_remaining) == 0:
            solutions.append(words)
        elif len(words) == max_len:
            return

        for word in self.words:
            if word[0] == words[-1][-1] and self._has_new_letters(word, letters_remaining):
                new_remaining = letters_remaining.copy()
                for letter in word:
                    if letter in new_remaining:
                        new_remaining -= {letter}
                        add_word = True
                if add_word:
                    self._add_solutions_with_words(words + [word], new_remaining, max_len, solutions)

    def find_solutions(self, max_len: int = 3) -> list[list[str]]:
        solutions = []
        all_letters = ""
        for side in self.sides:
            all_letters += side
        for word in self.words:
            letters_needed = {letter for letter in all_letters}
            for letter in word:
                if letter in letters_needed:
                    letters_needed -= {letter}
            self._add_solutions_with_words([word], letters_needed, max_len, solutions)
        return solutions


#lb = LetterBoxed(scraping.letters, scraping.todays_words)
#for solution in lb.find_solutions(3):
#    print(solution)
