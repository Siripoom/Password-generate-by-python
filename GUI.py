from cgitb import text
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from click import command
import main


def show_output():
    lenght = int(text_input.get())
    output = main.gen(lenght)

window = tk.Tk()    
window.title('Password Generator')
window.minsize(width=500, height=500)

title_label = tk.Label(master=window,text='Generate your password',font=40)
title_label.place(x=150,y=150)

text_input = tk.Entry(master=window)
text_input.place(x=200,y=200)

gen_button = tk.Button(
    master=window,text='Generate password',
    command=show_output
    )
gen_button.place(x=200,y=250)

output_label = tk.Label(master=window)
output_label.pack()


window.mainloop()


