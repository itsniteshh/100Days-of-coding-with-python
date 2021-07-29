import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
games = [rock, paper, scissors]

print("Enter 0 for rock, 1 for paper and 2 for scissors")
user_guess = int(input('Enter ur guess: '))
if user_guess == 0:
  print(f"You chose {games[0]}")
elif user_guess == 1:
  print(f"You chose {games[1]}")
else:
  print(f"You chose {games[2]}")

pc_guess = random.randint(0, len(games)-1)
print(f"PC chose: {games[pc_guess]}")

#conditionals
if user_guess == pc_guess:
  print("match drawn")
elif user_guess == 0 and pc_guess == 2:
  print("You win")
elif user_guess == 2 and pc_guess == 1:
  print("You win")
elif user_guess == 1 and pc_guess == 0:
  print("You win")
elif user_guess == 2 and pc_guess == 0:
  print("You Lose")
elif user_guess == 1 and pc_guess == 2:
  print("You Lose")
elif user_guess == 0 and pc_guess == 1:
  print("You Lose")
else:
  print("Invalid input")
