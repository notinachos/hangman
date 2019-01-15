#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A hangman clone, written in Python3 for the terminal. """

import codecs
import os
from random import choice

# a file containing ROT13 encoded words
word_file = 'words.txt'

# ascii main menu
game_menu = '''
 _____ 
||    |
||  _(xX)_
|| | [--] |
|| | [--] |
|| o |  | o
||   |  |
||   d  b
||
=============
H A N G M A N 
=============
(1) Start Game
(2) Add New Word
(3) Quit
'''

# ascii game board
# you can add extra "frames" here to make the game easier
game_board = [
'''
 _____ 
||    |
||
||
||
||
||
||
||
=============''',
'''
 _____ 
||    |
||   (oO)
||
||
||
||
||
||
=============''',
'''
 _____ 
||    |
||   (oO)
||   [--]
||
||
||
||
||
=============''',
'''
 _____ 
||    |
||   (oO)
||   [--]
||   [--]
||
||
||
||
=============''',
'''
 _____ 
||    |
||  _(oO)
|| | [--]
|| | [--]
|| o
||
||
||
=============''',
'''
 _____ 
||    |
||  _(oO)_
|| | [--] |
|| | [--] |
|| o      o
||
||
||
=============''',
'''
 _____ 
||    |
||  _(oO)_
|| | [--] |
|| | [--] |
|| o |    o
||   |
||   d
||
=============''',
'''
 _____ 
||    |
||  _(xX)_
|| | [--] |
|| | [--] |
|| o |  | o
||   |  |
||   d  b
||
=============''']


def main_menu():
    """ displays the main menu """
    os.system('cls||clear')
    choosing = True
    print(game_menu)
    while choosing:
        option = input('Pick an option: ')
        if option == '1':
            choosing = False
            os.system('cls||clear')
            game_loop()
        elif option == '2':
            choosing = False
            add_word()
        elif option == '3':
            choosing = False
        else:
            print('Invalid option! Try again.')


def add_word():
    """ adds new words to the game """
    choosing = True
    while choosing:
        new_word = input("Type the word you'd like to add: ")
        if len(new_word) < 4:
            print('Words must be at least 4 characters long. Try again.')
        else:
            choosing = False
            with open(word_file, 'a') as txt:
                txt.write('\n' + codecs.encode(new_word, 'rot_13').lower().rstrip().lstrip())
                input('New word "{}" has been added to the game!'.format(new_word.lower().rstrip().lstrip()))
            main_menu()


def game_loop():
    """ the main game loop. """

    # init some game variables
    game_over = False
    game_index = 0
    turn_counter = 0
    challenge_word = ''
    with open(word_file, 'r') as txt:
        lines = txt.read().splitlines()
        challenge_word = codecs.decode(choice(lines), 'rot_13')
    hidden_word = []
    guessed_letters = []

    while game_over == False:

        # update hidden word
        hidden_word = []
        for letter in challenge_word:
            if letter in guessed_letters:
                hidden_word.append(letter)
            else:
                hidden_word.append('_')

        # display game board
        print(game_board[game_index])

        # check if winner
        if '_' not in hidden_word:
            print('Congratulations, you won!')
            print('You correctly guessed the word: "{}" in {} turns.'.format(challenge_word, turn_counter))
            game_over = True
            break

        # check if loser
        if game_index == len(game_board) - 1:
            print('Game over, you lost!')
            print('You incorrectly guessed the word: "{}" in {} turns.'.format(challenge_word, turn_counter))
            game_over = True
            break

        # not winner/loser yet, so play ball
        game_status = 'Word:'
        for letter in hidden_word:
            game_status = game_status + ' ' + letter
        print(game_status)
        print('')
        game_status = 'Guessed Letters:'
        for letter in guessed_letters:
            game_status = game_status + ' ' + letter
        print(game_status)
        print('')

        # guess letter
        guessing = True
        while guessing:
            letter = input('Guess a letter: ').lower()
            if len(letter) != 1:
                print('Only guess one letter at a time. Guess again!')
            elif letter in guessed_letters:
                print('"' + letter + '" was already used. Guess again!')
            else:
                guessing = False
                guessed_letters.append(letter)
                turn_counter += 1
                if letter not in challenge_word:
                    game_index += 1
        os.system('cls||clear')


if __name__ == "__main__":
    main_menu()
    print('~ Thanks for playing! ~')
    exit(0)
