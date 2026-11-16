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

def decideOperation():
    """randomly chooses if teh operation is addition or subtraction"""
    return random.choice(['+','-'])

def displayMenu():
    """displays main ui"""

    #clears everything on the main win when player chooses to play again
    for widget in main.winfo_children():
        widget.destroy()

    #title
    title1 = tk.Label(main, text="Test your Math!",
                font = title_font
                ).pack(pady= 30)

    #difficulty levels - naming variables and assigning attributes and positioning
    dif1 = tk.Button(main, text="Easy",
                bg = 'green',
                font= button_font,
                width= 20,
                height= 2,
                command=lambda: open_questions("easy")).pack(pady= 10)
    dif2 = tk.Button(main, text="Intermediate",
                bg = 'yellow',
                font= button_font,
                width= 20,
                height= 2,
                command=lambda: open_questions('intermediate')).pack(pady= 10)
    dif3 = tk.Button(main, text='Advanced',
                bg='red',
                font= button_font,
                width= 20,
                height= 2,
                command=lambda: open_questions('advanced')).pack(pady= 10)


def displayProblem(q_label, answer_entry, attempt_label, state, difficulty):
    """creates random problems, is displayed and clears answer box. and returns the correct answer to the problem"""

    #a and b are assigned random numbers based on teh global dictionary's numebr range per difficulty
    a = randomint(difficulty) 
    b = randomint(difficulty)
    operation = decideOperation()

    if operation == '+': #simple conditional to determine addition or subtraction
        correct_answer = a + b
    else:
        correct_answer = a - b

    #sets the text in q_label to display the problem in this format
    q_label.config(text=f"Question {state['index'] + 1} of {TOTAL_QUES}\n\n{a} {operation} {b} =")

    attempt_label.config(text='First attempt = 10 points')
    answer_entry.delete(0,tk.END) #clears entry box for player convenience

    return correct_answer


def isCorrect(user_answer, correct_answer, attempt, parent):
    """checks player answer, then shows a message indicating if they were right or wrong"""
    #this conditional checks if the user's answer is correct, checks if it was submitted first or second try,
    #then prompts the appropriate amount of points
    if user_answer == correct_answer:
        points = FIRST_TRY if attempt == 1 else SECOND_TRY
        messagebox.showinfo("Result", f"Correct! + {points} points", parent=parent)
        return True #exits function immediately if answer is correct

    #only reached if answer is wrong
    #conditional checks if attempt is equal to 1, otherwise if the user misses their second chance, it prompts the appropriate message
    if attempt == 1:
        messagebox.showinfo("Result", "Wrong, one more try!", parent = parent)
    else:
        messagebox.showinfo("Result", f"Wrong! The answer was: {correct_answer}", parent=parent)

    return False



def get_rank(score):
    """converts the points into a letter rating"""
    #basic conditional statements covering the entry point of each rank
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"



    tk.Button(win, text='Submit', command=submit).pack(pady="10")
    show_question()








main.mainloop()