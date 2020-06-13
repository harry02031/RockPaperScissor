import random
print("Game Rules: Rock beats Scissor, Scissor beats Paper, Paper beats Rock")
print("Whoever gains 3 points first wins")
Playerpoints = 0
Computerpoints = 0
print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')

Roundnum = 1

while Playerpoints < 3 and Computerpoints < 3:

    print(f'Round {Roundnum} begins')
    decision = input("Make a move of either (rock) or (paper) or (scissor): ")
    if decision != 'rock' and decision != 'paper' and decision != 'scissor':
        print("Please make a valid move of either rock or paper or scissor")

    Roundnum += 1
    mydecision = random.randint(0, 2)

    if mydecision == 0:
       print("my move is rock")
    if mydecision == 1:
       print("my move is paper")
    if mydecision == 2:
       print("my move is scissor")

    if mydecision == 0 and decision == 'rock':
       print("its a tie!")
       print("Time for another round")
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')
    if mydecision == 0 and decision == 'paper':
       print("You win!")
       Playerpoints += 1
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')

    if mydecision == 0 and decision == 'scissor':
       print("You lose!")
       Computerpoints += 1
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')
    if mydecision == 1 and decision == 'rock':
       print("You lose!")
       Computerpoints += 1
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')
    if mydecision == 1 and decision == 'paper':
       print("It's a tie!")
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')
    if mydecision == 1 and decision == 'scissor':
       print("You win!")
       Playerpoints += 1
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')
    if mydecision == 2 and decision == 'rock':
       print("You win!")
       Playerpoints += 1
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')
    if mydecision == 2 and decision == 'paper':
       print("You lose!")
       Computerpoints += 1
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')
    if mydecision == 2 and decision == 'scissor':
       print("Its a tie!")
       print(f'Current Scoreboard is that You have {Playerpoints} points and I have {Computerpoints} points')

print("Game is over!")
if Computerpoints == 3:
    print(f'You lose the game since you have {Playerpoints} points and I have {Computerpoints} points')
elif Playerpoints == 3:
    print(f'Congratulations! You win the game! You have {Playerpoints} points and I have {Computerpoints} points')
