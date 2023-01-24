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

#Write your code below this line 👇

user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if user == "0":
    print (rock)
elif user == "1":
    print(paper)
elif user == "2":
    print(scissors)
else:
    print("You typed and invalid number")

if int(user) >= 0 and int(user) <= 2:
    print ("Computer choose:")
    comp_answer = random.randint(0,2)
    if comp_answer == 0:
        print(rock)
    elif comp_answer == 1:
        print(paper)
    else:
        print(scissors)

    outcome =int(user) - int(comp_answer)

    if outcome == -1 or outcome == 2:
        print("You Lose")
    elif outcome == -2 or outcome == 1:
        print("You Win!")
    else:
        print("Draw")
else:
    print("You lose")


