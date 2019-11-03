import random


def welcome():
    pass


def pick():
    with open('words.txt') as f:
        lines = f.readlines()
        word = random.choice(lines)
    return word


def guess(char, word, placeholder):
    p_list = list(placeholder)
    if char in word:
        for i in range(len(word)):
            if char == word[i]:
                p_list[i] = char
    return ''.join(p_list)


def play(word):
    placeholder = '_' * len(word)
    for i in range(10):
        user_guess = input("Guess Letter: ")
        placeholder = guess(user_guess, word, placeholder)
        print(placeholder)
        if placeholder == word:
            return True
    return False
