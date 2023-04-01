import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice:"))

    while choice > 3 or choice < 1:
        choice = int(input('\nEnter a valid choice please:'))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print('User choice is \n', choice_name)

    print('\nNow its Computers Turn....')

    comp= random.randint(1, 3)

    while comp == choice:
        comp = random.randint(1, 3)

    if comp == 1:
        compname = 'Rock'
    elif comp == 2:
        compname = 'Paper'
    else:
        compname = 'Scissor'
    print("Computer choice is \n", compname)
    print(choice_name, 'Vs', compname)

    if choice == comp:
        print('Its a Draw', end="")
        result = "Draw"

    elif (choice == 1 and comp == 2):
        print('paper wins =>\n', end="")
        result = 'Paper'
    elif (choice == 2 and comp == 1):
        print('paper wins =>\n', end="")
        result = 'Paper'

    elif (choice == 1 and comp == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp == 1):
        print('Rock wins =>\n', end="")
        result = 'Rock'

    elif (choice == 2 and comp == 3):
        print('\nScissors wins =>', end="")
        result = 'Scissor'
    elif (choice == 3 and comp == 2):
        print('\nScissors wins =>', end="")
        result = 'Rock'

    if result == 'Draw':
        print("<== Its a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("\nDo you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        print("Thanks for playing!")
        exit(False)

#import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice:"))

    while choice > 3 or choice < 1:
        choice = int(input('\nEnter a valid choice please:'))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print('User choice is \n', choice_name)

    print('\nNow its Computers Turn....')

    comp= random.randint(1, 3)

    while comp == choice:
        comp = random.randint(1, 3)

    if comp == 1:
        compname = 'Rock'
    elif comp == 2:
        compname = 'Paper'
    else:
        compname = 'Scissor'
    print("Computer choice is \n", compname)
    print(choice_name, 'Vs', compname)

    if choice == comp:
        print('Its a Draw', end="")
        result = "Draw"

    elif (choice == 1 and comp == 2):
        print('paper wins =>\n', end="")
        result = 'Paper'
    elif (choice == 2 and comp == 1):
        print('paper wins =>\n', end="")
        result = 'Paper'

    elif (choice == 1 and comp == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp == 1):
        print('Rock wins =>\n', end="")
        result = 'Rock'

    elif (choice == 2 and comp == 3):
        print('\nScissors wins =>', end="")
        result = 'Scissor'
    elif (choice == 3 and comp == 2):
        print('\nScissors wins =>', end="")
        result = 'Rock'

    if result == 'Draw':
        print("<== Its a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("\nDo you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        print("Thanks for playing!")
        exit(False)

