import random, sys

print("ROCK, PAPER, SISSORS")

# These variables keep track of the number of wins, looses and ties
wins = 0
looses = 0
ties = 0

while True:
    print('%s Wins, %s Looses, %s Ties' % (wins, looses, ties))
    while True: # The player input loop.
        print("Enter your move: (r)ock, (p)aper, (s)issors or (q)uit")
        playerMove = input('> ')
        if playerMove == 'q':
            print("Bye!")
            sys.exit(0) # quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break out of the player input loop
        print("Type one of r, p, s or q")
    
    # Display what the player chose:
    if playerMove == 'r':
        print("ROCK versus ...")
    elif playerMove == 'p':
        print("PAPER versus ...")
    elif playerMove == 's':
        print("SISSORS versus ...")  

    # Display what the computer choose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'        
        print("SISSORS")

    # Display and record the win/looses/tie
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You Win!")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You Win!")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print("You Win!")
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You Loose!")
        looses = looses + 1
    elif playerMove == 'p' and computerMove == 's':
        print("You Loose!")
        looses = looses + 1
    elif playerMove == 's' and computerMove == 'r':
        print("You Loose!")
        looses = looses + 1