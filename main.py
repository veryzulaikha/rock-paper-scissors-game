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

user_input = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n")
user_input_int = int(user_input)
if user_input_int == 0:
    print(f"You chose: {rock}")
if user_input_int == 1:
    print(f"You chose: {paper}")
if user_input_int == 2:
    print(f"You chose: {scissors}")

rock_paper_scissors = [rock, paper, scissors]
random_value = random.choice(rock_paper_scissors)

print(f"Computer chose: {random_value}")

if random_value == rock and user_input_int == 2:
    print("You lose!")

elif random_value == scissors and user_input_int == 1:
    print("You lose!")

elif random_value == paper and user_input_int == 0:
    print("You lose!")

elif random_value == paper and user_input_int == 1:
    print("draw!")

elif random_value == rock and user_input_int == 0:
    print("draw!")

elif random_value == scissors and user_input_int == 2:
    print("draw!")

else:
    print("You win!")

