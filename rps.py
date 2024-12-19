import random
option=["rock","paper","scissor"]
user_choice=(input("choose rock paper or scissors"))
computer_choice=random.choice(option)
print("You chose ",user_choice)
print("Computer chose ",computer_choice)
if user_choice==computer_choice:
    print("its a tie")
elif user_choice=="rock" and computer_choice=="scissor":
    print("Rock beats scissors so you win!")
elif user_choice=="scissor" and computer_choice=="rock":
    print("Rock beats scissors so computer wins!")
elif user_choice=="paper" and computer_choice=="rock":
    print("Paper beats rock so you win!")
elif user_choice=="rock" and computer_choice=="paper":
    print("Rock beats scissors so computer wins!")
elif user_choice=="paper" and computer_choice=="scissors":
    print("Rock beats scissors so computer wins!")
elif user_choice=="scissors" and computer_choice=="paper":
    print("Rock beats scissors so you win!")
else:
    print("You have entered something invalid")