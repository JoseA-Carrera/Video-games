import random


def run():
    random_number = random.randint(1, 100)
    number = int(input('choose a number: '))

    while number != random_number:
        if number < random_number:
            print('Choose a larger number')
        else:
            print('Choose a lower number ')
        number = int(input('\nchoose another number: '))

    print('\nCongratulations!')


if __name__ == '__main__':
    run()
