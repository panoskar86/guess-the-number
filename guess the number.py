Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> # template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#imports
import math
import random
import simplegui

#initialize global variables
range100 = True
range1000 = False
rem_guess = 7

# helper function to start and restart the game
def new_game():
    global secret_number
    
    print " "
    
    if range100 == True: 
            secret_number = random.randrange(0,100)
    else : 
            secret_number = random.randrange(0,1000)
            
    return "secret_number"

# define event handlers for control panel
# function range100
def range100():
    global range100, range1000
    print"New Game.Range of 0 to 100"
    range100 = True
    range1000 = False
    new_game()
   
    
# function range1000   
def range1000():
    global range100, range1000
    print"New Game.Range of 0 to 1000"
    range100 = False
    range1000 = True
    new_game()
    
#function input_guess    
def input_guess(guess):
    global rem_guess
    guess=int(guess)
    print "Guess was ",guess
    
    
    
    #if statement for remaining guesses and for the game
    if rem_guess > 1:
    
        if secret_number > guess: 
            print "Higher"
            rem_guess=rem_guess-1
            print "Remaining guesses ",rem_guess
            print " "
        elif secret_number < guess:
            print "Lower"
            rem_guess=rem_guess-1
            print "Remaining guesses ",rem_guess
            print " "
        elif secret_number==guess:
            print "Correct"
            print"Start a new game"
            print " "
            new_game()
            
    else :
        print"Out of guesses.Secret number was ",secret_number
        rem_guess = 7
  

    
#create window
f=simplegui.create_frame("Guess the number",200,200)

# create control elements
f.add_button("Range is (0,100)",range100,200)
f.add_button("Range is (0,1000)",range1000,200)
f.add_input("Enter a guess",input_guess,200)


# call new_game 
new_game()
