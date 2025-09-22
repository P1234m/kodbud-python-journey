#Task 2: Create a Number Guessing Game
'''Explanation:
•
Generate a random number between 1 and 100 using random module
•
Ask user to guess until correct
•
Show hints like "Too high" or "Too low"
Bonus: Count the number of attempts.'''

import random
import time
def play_game():
    print("Welcome to the Number Guessing Game!")
    #choosing difficulty level to make the game more interesting
    difficulty=input("Choose difficulty (Easy/Medium/Hard): ")
    ranges={'easy':50,'medium':100,'hard':150}
    max_num=ranges.get(difficulty,100)
    #choosing the random number
    number=random.randint(1,max_num)
    attempts=0
    guess=[]
    start_time=time.time()
    print(f"I am trying to think of number between 1 to {max_num}!")
    print("Guess the number!")

    while True:
        try:
            input_number=int(input("Enter the guessed number..."))
            attempts+=1
            guess.append(input_number)

            if(input_number<number):
                print("Too Low!")
            elif(input_number>number):
                print("Too High!")
            elif(input_number==number):
                time_required=round(time.time()-start_time,2)
                print("Perfect Guess")
                print(f"You guessed in {time_required}s time and {attempts} attempts")
                print(f"your guesses : {guess}")
                break
            #else:
               # print("Provide valid number")---->without using try except block

        except ValueError:
            print("Please enter valid number...")
    if input("Play again: (yes/no)").lower()=='yes':
        play_game()

play_game()