import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

#globals
COURSE_COUNT = 3
COURSE_MARK = 20
EXAM_MARK = 100 
TOTAL_MARK = COURSE_COUNT * COURSE_MARK + EXAM_MARK #out of 160

#data line layout for notes
#2345,Sam Sturtivant,14,15,14,77
#student code, name, course marks(3), exam marks

#to link the txt file
FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "studentMarks.txt")

#file handler
def load_student(filename):
    """this reads the student txt file - returnign back the student line, the problems in the line(invalid values or characters), and the countline"""
    students = []
    problem = []
    count_line = False

    #this fires IF the txt file is not available locally
    if not os.path.exists(filename):
        return student, True, [f"Could not find the file:\n{filename}\nIt will be created when you save a change."]

    #reads and opens the txt file - strips down every line too
    with open(filename, 'r', encoding = 'utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    #splits all the data into
    for position, line in enumerate(lines):
        parts = [part.strip() for part in line.split(",")]

        if position == 0 and len(parts) == 1 and parts[0].isdigit():
            count_line = True
            continue

        try:
            if len(parts) != 2 + COURSE_COUNT + 1:
                raise ValueError
            student.append({
                "number": parts[0],
                "name": parts[0],
                "coursework": [int(mark) for mark in parts [2:2 + COURSE_COUNT]],
                "exam": parts[-1]
            })
        except ValueError:
            problem.append(f"Line {position +1} skipped: {line}")

    return student, count_line, problem

def student_save(filename, students, count_line):
    lines = []
    if count_line:
        lines.append(str(len(students)))
    for student in students:
        parts = [student['number'], student['name']]
        parts += [str(mark) for mark in student['coursework']]



    

#functions for calculating
def course_total(student):
    """returns total coursework marks"""
    return sum(student['coursework'])

def score_total(student):
    """returns total of exam + course marks"""
    return course_total('student') + student['exam']