import random

'''for i in range(10):
  j=random.randint(1,6)
  print(j)'''
  
lstPlayerRolls1 = []
lstPlayerRolls2 = []
  
for i in range(10):
  rollPlayer1 = random.randint(1, 12)
  print('Player1 rolled: ', rollPlayer1)
  lstPlayerRolls1.append(rollPlayer1)

scorePlayer1 = sum(lstPlayerRolls1)
print()
print("Player1 score: ", scorePlayer1)

print()

for i in range(10):
  rollPlayer2 = random.randint(1, 12)
  print('Player2 rolled: ', rollPlayer2)
  lstPlayerRolls2.append(rollPlayer2)

  
scorePlayer2 = sum(lstPlayerRolls2)
print()
print("Player2 score: ", scorePlayer2)

print()

if scorePlayer1 > scorePlayer2:
  print('Player1 Wins!')
elif scorePlayer1 < scorePlayer2:
  print('Player2 Wins!')
elif scorePlayer1 == scorePlayer2:
  print('Its a Tie!')
