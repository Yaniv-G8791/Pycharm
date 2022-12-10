
from pickle import TRUE
import random
def game(user_choice):
    COMPCHOICE=random.choice(['scissors','paper','rock'])
    user_choice=user_choice.lower()
    if COMPCHOICE==user_choice:
     print('tie')
    elif user_choice== 'rock' and COMPCHOICE=='scissors':
     print('WIN '+user_choice + ' is stronger than ' + COMPCHOICE)
    elif user_choice== 'rock' and COMPCHOICE=='paper':
     print('LOSE '+COMPCHOICE + ' is stronger than ' + user_choice)
    elif user_choice== 'scissors' and COMPCHOICE=='paper':
     print('WIN '+user_choice + ' is stronger than ' + COMPCHOICE)
    elif user_choice== 'scissors' and COMPCHOICE=='rock':
     print('LOSE '+COMPCHOICE + ' is stronger than ' + user_choice)
    elif user_choice== 'paper' and COMPCHOICE=='rock':
     print('WIN '+user_choice + ' is stronger than ' + COMPCHOICE)
    elif user_choice== 'paper' and COMPCHOICE=='scissors':
     print('LOSE '+COMPCHOICE + ' is stronger than ' + user_choice)
    else:
     print('you lose :(')


flag=True
while(flag == True):
    user_choice=input('Do you want - rock, paper or scissors?\n')
    game(user_choice)
    another_game=input('type Y for another game? ')
    if(another_game.lower() == "y"):
        flag=True
    else:
        flag=False