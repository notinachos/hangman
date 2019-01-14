#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A hangman clone, written in Python3 for the terminal. """

import codecs
import os
from random import choice

# I searched for the hardest hangman words and encoded them ROT13
# so that reading the code wouldn't give away all the answers ;)
words = [
    'noorl', 'noehcgyl', 'nssvk', 'nfxrj', 'nkvbz', 'nmher', 'ontcvcrf', 'onaqjntba', 
    'onawb', 'onlbh', 'ovxvav', 'oyvgm', 'obbxjbez', 'obkpne', 'obkshy', 'ohpxnebb', 
    'ohssnyb', 'ohssbba', 'pbojro', 'pebdhrg', 'qnvdhvev', 'qvfnibj', 'qhcyrk', 'qjneirf', 
    'rdhvc', 'rkbqhf', 'svfuubbx', 'svknoyr', 'sbktybir', 'tnynkl', 'tnyinavmr', 'tnmrob', 
    'tvmzb', 'tybjjbez', 'thssnj', 'unvxh', 'uncunmneq', 'ulcura', 'vprobk', 'vawhel', 'vibel', 
    'vil', 'wnhaqvpr', 'wnjoernxre', 'wnljnyx', 'wnmml', 'wvtfnj', 'wvhwvgfh', 'wbpxrl', 'wbivny', 
    'wblshy', 'whvpl', 'whzob', 'xnmbb', 'xrlubyr', 'xunxv', 'xvybolgr', 'xvbfx', 'xvjvsehvg', 
    'xancfnpx', 'ynelak', 'yhkhel', 'znedhvf', 'zrtnuregm', 'zvpebjnir', 'zlfgvsl', 'avtugpyho', 
    'abjnqnlf', 'ahzofxhyy', 'binel', 'bkvqvmr', 'bkltra', 'cnwnzn', 'crrxnobb', 'cvkry', 'cvmnmm', 
    'carhzbavn', 'cbyxn', 'dhnegm', 'dhvm', 'dhbehz', 'enmmzngnmm', 'euhoneo', 'evpxfunj', 
    'fpuvmbcueravn', 'fcuvak', 'fcevgm', 'fdhnjx', 'fhojnl', 'fjviry', 'gbcnm', 'haxabja', 'hajbegul', 
    'hamvc', 'hcgbja', 'incbevmr', 'ivkra', 'ibqxn', 'ibegrk', 'jnyxjnl', 'jnygm', 'jnil', 'jnkl', 
    'jurrml', 'juvfxrl', 'jubzrire', 'jvzcl', 'jvmneq', 'jbbml', 'klybcubar', 'lnpugfzna', 'lvccrr', 
    'lbhgushy', 'mrcule', 'mvtmnt', 'mvypu', 'mbqvnp', 'mbzovr', 'ihyarenovyvgl ', 'havagrerfgvat ', 
    'furrcureqvat ', 'pbaqbzvavny ', 'fcrezbculgr', 'ntabfgvp', 'pryyhybfr', 'cubgbflagurfvf', 
    'culfvbgurencl', 'ylak', 'tvenssr'
]

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
============''',
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
============''',
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
============''',
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
============''',
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
============''',
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
============''',
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
============''',
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
============''']


def game_loop():
    """ the main game loop. """

    # init some game variables
    game_over = False
    game_index = 0
    turn_counter = 0
    challenge_word = codecs.decode(choice(words), 'rot_13')
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
    os.system('cls||clear')
    game_loop()
    print('~ Thanks for playing! ~')
    exit(0)
