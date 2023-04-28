import tkinter as tk
from tkinter import Frame

#quit subroutine
def quit():
    root.destroy()

#print details of all the camps
def print_camp_details():
    global j_names, total_entries, name_count = 0 

root = tk.Tk()  #so this is my 'my_window'

root.geometry("500x500")
root.title("Sunshine Camp Adventure")

label = tk.Label(root, text="Hello Camper!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 20))
textbox.pack()

myentry = tk.Entry(root)
myentry.pack(padx=20)

#button = tk.Button(root, text='ENTER', font=('Arial', 18))
#button.pack(padx=5, pady=10)

buttonframe: Frame = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')



#anotherbtn = tk.Button(root, text='TEST')
#anotherbtn.place(x=200, y=200, height=100, width=100)
#you can use place instead of pack or grid to put stuff(widgets) excatly where you want
#tkinter works by import module, create root window, add widgets, choose layout eg. grid, pack, place function
#now we just add functionality eg. button clicks,or certain widgets, so its functional and more than just a design

#def quit():
#   main_window.destroy()

root.mainloop()
