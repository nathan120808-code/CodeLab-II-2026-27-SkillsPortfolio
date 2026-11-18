from tkinter import * #imports everything from tkinter module

root = Tk() #assigns the tkinter library to a variable

#label widget

root.title('Deeznuts') #sets the name of the app

root.geometry('900x600') #sets windw size preset on launch

root.resizable(0,0) #mkes window size is fixed and unadjustable

root.configure(bg="black")

custom_font = ("consolas", 50, "italic")


text1 = Label(root,text="I want butter chicken",
                fg = "white",
                bg = "black",
                font= "Sans, 25")

text2 = Label(root,text="only 13 aed pls",
                fg = "red",
                bg = "black",
                font= custom_font,
                pady = 20)
text1.pack()
text2.pack()


root.mainloop() #mainloop indicates the app is ready to run and tells the code to be displayed
