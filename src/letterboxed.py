import argparse, sys
from lb_logic import LetterBoxed
import scraping


def validate_sides(sides: str, error_message: str):
    if not isinstance(sides, str):
        print(error_message)
        sys.exit()

    num_sides = 0
    for side in sides.split('-'):
        if len(side) != 3:
            print(error_message)
            sys.exit()
        num_sides += 1

    if num_sides != 4:
        print(error_message)
        sys.exit()




def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--today', action='store_true', help="Uses today's puzzle")
    group.add_argument('-s', '--sides', default='', type=str,
                        help='Specifies the sides of the puzzle in the format abc-def-ghi-jkl')
    parser.add_argument('-m', '--max', default='3', type=int, help='Specify the max number of words in a solutions')
    args = parser.parse_args()

    if args.today:
        lb = LetterBoxed(scraping.letters, scraping.todays_words)
        for solution in lb.find_solutions(args.max):
            print(" + ".join(solution))
    else:
        validate_sides(args.sides, "The sides of the puzzle must be given in the format abc-def-ghi-jkl")
        words = []
        with open("standard_dictionary.txt", "r") as dict_words:
            for word in dict_words.readlines():
                words.append(word.strip())
        lb = LetterBoxed(args.sides, words)
        for solution in lb.find_solutions(args.max):
            print(" + ". join(solution))



if __name__ == "__main__":
    main()