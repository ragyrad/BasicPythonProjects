from random import choice

# Random word list
WORDS = ['breath', 'apple', 'queen', 'country', 'airport', 'actor', 'night', 'expression', 'town', 'agency']


def choose_word():
    pass


def is_guessed(word, word_with_closed_letters):
    pass


def check_letter(l, word):
    pass


def unlock_letter(l):
    pass


def main():
    word, word_with_closed_letters = choose_word()
    number_of_guessed_letters = 0
    hp = len(word) + 5
    print("Welcome to HANGMAN\n"
          "The goal of the game is to guess the hidden word")
    print(f"The are {len(word)} letters in a word")
    game_is_running = True
    while hp > 0:
        if not is_guessed(word, word_with_closed_letters):
            print(f"{hp} HP left")
            print(f"Word: {*word_with_closed_letters}")
            letter = input("Guess the letter: ")
            if check_letter(letter, word):
                word_with_closed_letters = unlock_letter(letter)
            else:
                hp -= 1
        else:
            print("Congratulations! You won!")
            break
    else:
        print("GAME OVER")
