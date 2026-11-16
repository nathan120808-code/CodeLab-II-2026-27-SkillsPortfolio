#library imports
import random
import tkinter as tk
from tkinter import messagebox

#essentials
main = tk.Tk()
main.title("Math Game")
main.geometry('800x500')
main.resizable(0,0)
main.configure(
    bg='black'
)

# global variables for customization
title_font = ('Helvetica', 40, 'bold')
button_font = ('Monospace', 15)

#GLOBAL VARIABLES
#settings for the game
TOTAL_QUES = 10 #10 times 10 equaes to 100 - the maximum score in quiz
FIRST_TRY = 10 #will be multiplied against total/ 10 points for first try
SECOND_TRY = 5 #will be multiplied against total/ 5 points on second

#this sets the range of the questions - easy means single digit numbers to be solved, moderate means double - so on so forth
RANGES = {
    'easy':(1,9),
    'moderate':(10,99),
    'advanced':(1000,9999)
}

#FUNCTIONS

def randomint(difficulty):
    """returns rnadom number, min max depends on the difficult"""
    low, high = RANGES[difficulty]
    return random.randint(low,high)

def decideOp():
    """randomly chooses if teh operation is addition or subtraction"""
    return random.choice(['+','-'])









main.mainloop()