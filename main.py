import re


def Hangman():
    my_secret_word = input('Write down your secret word: ')
    mistakes = 0
    mistakes_allowed = 7
    result = ['*'] * len(my_secret_word)

    print(result)

    while True:
        letter_guess = input('Guess the letter: ')
        for letter in letter_guess:
            if letter.lower() in my_secret_word.lower():
                indexes_list = [i.start() for i in re.finditer(letter.lower(), my_secret_word.lower())]
                for x in indexes_list:
                    result[x] = my_secret_word[x]

            elif letter.lower() not in my_secret_word.lower():
                mistakes += 1

        print(f'Mistakes left: {mistakes_allowed - mistakes}')
        if '*' not in result:
            print('You won!')
            print(f'The conceived word was {my_secret_word.upper()}!')
            Hangman()

        if mistakes >= mistakes_allowed:
            print('You lost!')
            print(f'The conceived word was {my_secret_word.upper()}!')
            Hangman()

        if letter_guess.lower() == 'exit':
            print(f'The conceived word was {my_secret_word.upper()}!')
            exit()

        print(result)


Hangman()
