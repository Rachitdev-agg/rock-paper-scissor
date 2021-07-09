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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
signs = [rock, paper, scissors]
pc = random.randint(0, 2)
if user == 0:
  print(rock)
  if pc == 1:
    print(paper)
    print("You lose")
  elif pc == 2:
    print(scissors)
    print("You win")
  else:
    print(rock)
    print("Draw")
elif user == 1:
  print(paper)
  if pc == 0:
   print(rock)
   print("You win")
  elif pc == 2:
   print(scissors)
   print("You lose")
  else:
    print(paper)
    print("Draw")
elif user == 2:
  print(scissors)
  if pc == 0:
   print(rock)
   print("You lose")
  elif pc == 1:
   print(paper)
   print("You win")
  else:
    print(scissors)
    print("Draw")
else:
  print("Please select a valid number")

