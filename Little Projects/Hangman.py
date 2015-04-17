import random


def start():
    play_game = True
    while play_game is True:
        play_game_2 = input('Would you like to play again? ')
        if play_game_2 == 'yes' or 'y':
            print('Ok, lets play again!')
        elif play_game_2 == 'no' or 'n':
            print('Ok, thanks for playing')
            play_game = False
        else:
            print('That is not a valid input')


def pick_word():
    f = open('Hangman Words')
    print(f.readline())
    f.close()


word = 'jungle'
guessed_letters = []
hangman_list = []
hangman_word = ''
guesses = 0

for letter in word:
    hangman_list += '_'

for item in hangman_list:
    hangman_word += item

while guesses < 6:
    print('This is your word: ' + hangman_word)
    print('It is ' + str(len(word)) + ' letters long')
    letter = input('Please guess a letter: ')
    if letter in guessed_letters:
        print('You\'ve already guessed that letter!')
        continue
    else:
        guessed_letters.append(letter)
        index = 0
        while index < len(word):
            if word[index] == letter:
                hangman_list[index] = letter
                hangman_word = ''
                for item in hangman_list:
                    hangman_word += item
            index += 1
        guesses += 1
        print('You\'ve made ' + str(guesses) + ' guesses. You can have a maximum of 6 guesses')
    if '_' not in hangman_list:
        print('You guessed the word!')
        break
