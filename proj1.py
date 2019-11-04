import random


def welcome():
    pass


def pick():
    with open('words.txt') as f:
        lines = f.readlines()
        word = random.choice(lines).strip()
    return word


def guess(char, word, placeholder, attempts):
    p_list = list(placeholder)
    if char in word:
        for i in range(len(word)):
            if char == word[i]:
                p_list[i] = char
    else:
        attempts -= 1
    return ''.join(p_list), attempts


def play(word):
    placeholder = '-' * len(word)
    attempts = 10
    while attempts > 0:
        user_guess = input("Guess Letter: ").capitalize()
        placeholder, attempts = guess(user_guess, word, placeholder, attempts)
        print(placeholder)
        if placeholder == word:
            print('Win')
            return True
        print("Attempts: ", attempts)
    return False


def main():
    welcome()
    while True:
        word = pick()
        win = play(word)

main()
