# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

number_range = 100
secret_number = 0
counter = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global counter
    global secret_number
    global number_range
    
    secret_number = random.randrange(0,number_range)
    
    if number_range == 100:
        counter = 7
    elif number_range == 1000:
        counter = 10
        
    print("New game. Range is from 0 to", number_range, ".Best of luck")
    print("No. of remaining guesses is: " + counter + "\n")


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_range
    number_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number_range
    number_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global counter
    
    won = False
    
    print("You guessed", guess)
    counter -= 1
    print("Number of remaining guesses is:", counter)
    
    if int(guess) == secret_number:
        won = True
    
    elif int(guess) > secret_number:
        result = "Lower"
    else:
        result = "Higher"
        
        
    if won:
        print("You guessed the correct no. " + guess + "\n")
        new_game()
        return
    
    elif counter == 0:
        print("Ran out of guess, hence failed")
        new_game()
        return
    
    else:
        print(result)        

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess: ", input_guess, 200)

    
frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
