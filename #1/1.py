import random

def checkGuess(guess, awnser):
    resp = ''
    for i in range(3):
        for j in range(3):
            if awnser[i] == guess[j] and i==j: 
                resp = resp + 'Fermi '
            elif awnser[i] == guess[j]: 
                resp = resp + 'Pico '
    if resp == '': 
        resp = 'Bagels'
    if resp == 'Fermi Fermi Fermi ' : 
        resp = 'You got it!'
    return resp


def theGame():
    print(""" 
        Bagels, a deductive logic game.
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
    """)
    awnser = ''
    for i in range(3): 
        awnser += str(random.randint(0, 9))
    for i in range(1,11):
        print('#Guess{}:'.format(i))
        try:
            guess = input('> ')
            if len(guess) != 3:
                raise ValueError("Your guess must be a 3-digit number!!!!")
        except ValueError as e:
            print(e)
            continue

        flag = checkGuess(guess,awnser)
        if flag == 'You got it!':
            print(flag)
            break
        print(flag)

def main():
    while True:
        theGame()
        response = input("Do you want to play again? (yes or no)")
        if response.lower() != 'yes':
            break
    print("Thanks for playing!")

main()



