import random

r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
  
  choices = ["rock", "paper", "scissor" ]
  computer_choice = random.choice(choices)
  user_choice = None
  
  while user_choice not in choices:
    user_choice = input("What do you choose? Type Rock, Paper or Scissor: ").lower() 
    if user_choice == computer_choice:
      print("Computer Choice: ", computer_choice)
      print("Your Choice: ", user_choice)
      print("Its a Tie")
  
    elif user_choice == "rock":
      if computer_choice == "paper":
        print ("Computer Choice:", p)
        print ("Paper smashes Rock, You Lost 😞")
  
      elif computer_choice == "scissor":
        print ("Computer Choice:", s)
        print ("Rock smashes Scissor, You Won 🚀")
  
    elif user_choice == "paper":
      if computer_choice == "rock":
        print ("Computer Choice:", r)
        print ("Paper smashes Rock, You Won 🎉")
  
      elif computer_choice == "scissor":
        print ("Computer Choice:", s)
        print ("Scissor smashes Paper, You Lost 😭")
  
    elif user_choice == "scissor":
      if computer_choice == "rock":
        print ("Computer Choice:", r)
        print ("Rock smashes Scissor, You Lost 🥹")
  
      elif computer_choice == "paper":
        print ("Computer Choice:", p)
        print ("Scissor smashes Paper, You Won 🍸")

  play_again = input("Do you want to play again? (Yes/No) ").lower()
  if play_again != "yes":
    break

print("Goodbye 🙋")
        
