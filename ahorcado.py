import os
import random


def run():
    db = ['python', 'java', 'javascrip', 'kotlin', 'php', 'go', 'ruby']
    ascii = [
        '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
        '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
        '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
        '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
        '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
        '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
        '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    ]

    word = random.choice(db)
    spaces = ['_'] * len(word)
    attemps = 6

    while True:
        os.system('clear')

        for character in spaces:
            print(character, end=' ')

        print(ascii[attemps])
        letter = input('choose a letter: ').lower()

        found = False

        for i, character in enumerate(word):
            if character == letter:
                spaces[i] = letter
                found = True

        if not found:
            attemps -= 1

        if '_' not in spaces:
            os.system('clear')
            print('you win!')
            break
            input()

        if attemps == 0:
            os.system('clear')
            print('you lose!')
            print(f'the correct word is: {word}')
            break
            input()


if __name__ == '__main__':
    run()
