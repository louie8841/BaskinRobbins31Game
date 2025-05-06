from random import randint

current_number = 0
username = input('Who are you? ')
pl = ['u', 'c']
player = None

class Computer:
    def __init__(self):
        self.num = None
    def getNum(self):
        self.num = randint(1, 3)

class User:
    def __init__(self):
        self.num = None
    def getNum(self):
        while True:
            try:
                self.num = int(input('Enter a number (1 ~ 3): '))
                if 1 <= self.num <= 3:
                    break
                else:
                    print("Please enter a number between 1 and 3.")
            except:
                print("Invalid input. Try again.")

def addNum(n):
    global current_number
    for i in range(1, n+1):
        print(f"{current_number + i}! ", end='')
    print()
    current_number += n

def getFirstP():
    firstP = input(f"Who will be first (computer:c, {username}:p)? ")
    while firstP.lower() != 'c' and firstP.lower() != 'p':
        print('Please try again.')
        firstP = input(f"Who will be first (computer:c, {username}:p)? ")
    return firstP.lower() == 'p'

def runGame():
    global current_number, player
    current_number = 0  # Reset the number every game
    p = User()
    c = Computer()
    
    if getFirstP():
        while current_number < 31:
            player = pl[0]
            p.getNum()
            addNum(p.num)
            if current_number >= 31:
                break
            player = pl[1]
            c.getNum()
            print(f"Computer chose: {c.num}")
            addNum(c.num)
    else:
        while current_number < 31:
            player = pl[1]
            c.getNum()
            print(f"Computer chose: {c.num}")
            addNum(c.num)
            if current_number >= 31:
                break
            player = pl[0]
            p.getNum()
            addNum(p.num)

    if player == 'u':
        print(f'{username} lost')
    else:
        print(f'{username} won!')

    again()

def again():
    yn = input('Do you want to play again? (y/n): ')
    if yn.lower() == 'y':
        runGame()

runGame()
