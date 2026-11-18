import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

#globals
TOTAL_MARK = 160 #out of 160

#data line layout for notes
#2345,Sam Sturtivant,14,15,14,77
#student code, name, course marks(3), exam marks

#each student is a dict
# {"number": studentid, "name": "studentname", "marks": [1,2,3], "exam": 100}

#to link the txt file
FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "studentMarks.txt")

#file handler
def load():
    """reads txt file and loads liens into dictionaries"""
    students =[]
    if not os.path.exists(FILE):
        return students
    with open(FILE) as f:
        lines = f.read().splitlines()[1:] #skip line 1
    for line in lines:
        if line.strip():
            p = line.split(",")
            #splits the data seperately into their corresponding class
            students.append({"number": int(p[0]),
                            "name": p[1],
                            "marks": [int(m) for m in p[2:5]],
                            "exam": int(p[5])})

    return students

def save():
    """writes whole list back to the txt file"""
    with open(FILE, "w") as f:
        f.write(f"{len(students)}\n")
        for s in students:
            parts = [str(s["number"]),
                      s["name"] + [str(m) for m in s["marks"]] + [str(s["exam"])]]
            f.write(",".join(parts) + "\n")


#functions for calculating
def course_total(s):
    """returns total coursework marks"""
    return sum(s["marks"]) + s["exam"]

def score_total(s):
    """returns total of exam + course marks"""
    return course_total(s) / TOTAL_MARK * 100

def grade_total(s):
    st = score_total(s)
    if st >= 70:
        return "A"
    if st >= 60:
        return "B"
    if st >= 50:
        return "C"
    if st >= 40:
        return "D"
    return "F"

#backend functionality
def show_student(records, summar=''):
    """every menu item prints through here with the same format - displaying all relevant student details"""
    output.delete("1.0", tk.END)
    for s in records:
        output.insert(tk.END, f"{s['name']} ({s['number']}) Coursework: {sum(s['marks'])}/60"
                      f"Exam: {s['exam']}/100 Overall: {score_total(s):.1f}% Grade: {grade_total(s)}\n")

def has_students():
    """"""
    if not students:
        messagebox.showinfo("No data", "Please check if student records is in the local folder")

#FRONTEND

main = tk.Tk()
main.title("Student Manager")
main.geometry("800x500")
main.resizable(0,0)
main.config(
    bg = "#323B4E"
)

title_label = tk.Label(main, text="Student Manager")

