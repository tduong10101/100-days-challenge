import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)
art=[rock,paper,scissors]

if player == computer:
    result = "It's a draw"
elif player - computer == 1 or player - computer == -2:
    result = "You win"
else:
    result = "You lose"

print(f"{art[player]}\nComputer chose:\n{art[computer]}\n{result}") 