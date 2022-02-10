# Josh Park
# January 13, 2022
#Rock paper and scissors game
from random import randint #Importing the function randint and sleep
from time import sleep

#The actual game below is made by just running the function decide_winner, that we are def ining below 


def decide_winner():
    user_score = 0 #sets score to zero
    
    computer_score = 0
    
    while user_score < 3 and computer_score < 3 : #To make sure the game is out of three
        
        user_choice = input("Choose between rock paper scissors") #Your choice of rock paper or scissors
        
      
        options = ["R","P","S"] #Computer selects radomly from randint to decide its options
        computer_choice = options[randint(0,2)]

        print('Computer selecting') #Loading Screen
        sleep(1)
        print(computer_choice)
        sleep(1)
        if user_choice == computer_choice: #How the computer decides if the player or computer won
            print("It is a tie!")
        elif user_choice == "P" and computer_choice == "R":
            print("User Wins")
            user_score = user_score + 1
        elif user_choice == "S" and computer_choice == "P":
            print("User Wins")
            user_score = user_score + 1
        elif user_choice == "R" and computer_choice == "S":
            print("User Wins")
            user_score = user_score + 1
        else:
            print("User loses")
            computer_score = computer_score + 1  
        print("User Score: " + str(user_score) + " - " + "Computer Score: " + str(computer_score)) #Displays current score
        
    if user_score == 3: #Displays if you won the overall game or not
        print("you win the game")
    else: 
        print("you lose the game")
    
    
decide_winner()        #Runs the game with the function decide_winner











