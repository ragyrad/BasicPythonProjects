from random import choice

# Random word list
WORDS = ['breath', 'apple', 'queen', 'country', 'airport', 'actor', 'night', 'expression', 'town', 'agency']


def choose_word(word_list: list) -> tuple[list, list]:
    """The function randomly selects a word from the list and returns a tuple of two lists,
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
    """Accepts a secret word and a word in which the user opens the letters,
     if all the letters are guessed, then returns True, otherwise - False

    :param word: secret word
    :param word_with_closed_letters: word where user opens the letters
    :return: True if all letters is guessed and False if not
    """
    return word == word_with_closed_letters


def check_letter(letter: str, word: list):
    """Checks if there is a letter in a word. If present, returns the index of this letter.
    If there is no letter in the word returns -1.

    :param letter: the letter the player said
    :param word: secret word
    :return: Index of letter
    """
    # Make a list of indices in case a letter occurs several times in a word
    indexes = []
    for _ in range(word.count(letter)):
        if len(indexes) > 0:
            indexes.append(word.index(letter, indexes[-1] + 1))
        else:
            indexes.append(word.index(letter))
    if len(indexes) == 0:
        return -1
    else:
        return indexes


def unlock_letter(letter, secret_word, word: list) -> list:
    """opens the letter in the word that the player guessed

    :param letter: the letter the player said
    :param secret_word: secret word with unlocked letters
    :param word: word where user opens the letters
    :return: word with the open letter
    """
    for i in letter:
        word[i] = secret_word[i]
    return word


def main():
    word, word_with_closed_letters = choose_word(WORDS)
    # heals points equals the length of the word plus five
    hp = len(word) + 5
    print("Welcome to HANGMAN\n"
          "The goal of the game is to guess the hidden word")
    print(f"The are {len(word)} letters in a word")
    while hp > 0:
        print("\n", "="*20, "\n", sep="")
        if not is_guessed(word, word_with_closed_letters):
            print(f"{hp} HP left")
            print(f"Word:")
            print(*word_with_closed_letters)
            letter = input("Guess the letter: ")
            guessed_letter = check_letter(letter, word)
            if guessed_letter != -1:
                word_with_closed_letters = unlock_letter(guessed_letter, word, word_with_closed_letters)
            else:
                hp -= 1
                print("You didn't guess.")
        else:
            print("Congratulations! You won!")
            break
    else:
        print("GAME OVER")


if __name__ == '__main__':
    main()
