from random import choice

# Random word list
WORDS = ['breath', 'apple', 'queen', 'country', 'airport', 'actor', 'night', 'expression', 'town', 'agency']


def choose_word(word_list: list) -> tuple[list, list]:
    """the function randomly selects a word from the list and returns a tuple of two lists,
     where the first list is the selected word, and the second is the same word only with hidden letters

    :param word_list: list from which the word is selected
    :return: tuple of selected word and word with hidden letters
    """
    # Word as a list where each letter is an element of the list
    word = [*choice(word_list)]
    # Make a list of the same word, only hide the letters with the "_"
    hidden_letters = ['_']*len(word)
    return word, hidden_letters


def is_guessed(word: list, word_with_closed_letters: list) -> bool:
    """accepts a secret word and a word in which the user opens the letters,
     if all the letters are guessed, then returns True, otherwise - False

    :param word: secret word
    :param word_with_closed_letters: word where user opens the letters
    :return: True if all letters is guessed and False if not
    """
    return word == word_with_closed_letters


def check_letter(l, word):
    pass


def unlock_letter(l, word):
    pass


def main():
    word, word_with_closed_letters = choose_word(WORDS)
    hp = len(word) + 5
    print("Welcome to HANGMAN\n"
          "The goal of the game is to guess the hidden word")
    print(f"The are {len(word)} letters in a word")
    while hp > 0:
        if not is_guessed(word, word_with_closed_letters):
            print(f"{hp} HP left")
            print(f"Word:")
            print(*word_with_closed_letters)
            letter = input("Guess the letter: ")
            guessed_letters = check_letter(letter, word)
            if guessed_letters != -1:
                word_with_closed_letters = unlock_letter(guessed_letters, word_with_closed_letters)
            else:
                hp -= 1
        else:
            print("Congratulations! You won!")
            break
    else:
        print("GAME OVER")
