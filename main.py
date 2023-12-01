import random


def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def word_select():
    words = ['devops', 'mouse', 'green', 'networking', 'keyboard', 'coding']
    return random.choice(words)


def scramble_game():
    word = word_select()
    scrambled_word = scramble_word(word)

    print("Welcome to the game of Scramble!")
    print("Unscramble the word:", scrambled_word)

    guess = input("Your guess: ")

    if guess.lower() == word:
        print("Congratulations! You guessed it right!")
    else:
        print(f"Wrong! The correct word was '{word}'.")


scramble_game()
