# Author: Davide Pollicino
# Date: 17/11/2019

# Package for GUI implementation

import tkinter
from tkinter import *

window = Tk()

# Creates the window from the imported Tkinter module of dimension 800px X 8000px
window.geometry("800x800")

def window_content():
    # Adds a title to the Windows GUI for the window
    window.title("Student system ")
    # Set background color of the windows
    window.configure(background='green')

    lblName = Label(window, text='Name')
    lblName.grid(row=0, column=0, padx=10, pady=10)

    txtBoxName = Entry(window,bd=5)
    txtBoxName.grid(row=0, column=1, padx=10, pady=10)

    lblSurname = Label(window, text='Surname')
    lblSurname.grid(row=0, column=3, padx=10, pady=10)

    txtBoxSurname = Entry(window, bd=5)
    txtBoxSurname.grid(row = 0 ,column = 4, padx=10, pady=10)

    lblAge = Label(window,text='Age')
    lblAge.grid(row = 1 ,column = 0, padx=10, pady=10)

    txtBoxAge = Entry(window, bd=5)
    txtBoxAge.grid(row=1, column=1, padx=10, pady=10)

    lblAddress = Label(window, text='Address')
    lblAddress.grid(row =1, column=3, padx=10, pady=10)

    txtBoxAddress = Entry(window, bd=5)
    txtBoxAddress.grid(row=1,column=4, padx=10, pady=10)

    lblEmail = Label(window, text='Email')
    lblEmail.grid(row=2 , column = 0, padx=10, pady=10)

    txtBoxEmail = Entry(window, bd=5)
    txtBoxEmail.grid(row=2, column=1, padx=10, pady=10)

    lblNationalionality = Label(window ,text = 'Nationality')
    lblNationalionality.grid(row=2, column=3, padx=10, pady=10)

    txtBoxNationality = Entry(window , bd=5)
    txtBoxNationality.grid(row=2, column=4, padx=10, pady=10)

    btnSave = Button(window, text="Save", command=saveDetails())
    btnSave.grid(row=3 , column=1, padx=10, pady=10)

    btnClear = Button(window, text='Clear', command=clearPage())
    btnClear.grid(row=3, column=4, padx=10, pady=10)

    return

window_content()


window.mainloop()
# Loops the window to prevent the window from just "flashing once"





