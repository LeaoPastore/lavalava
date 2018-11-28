def readfile(file):
    f = open (file , 'r')
    a = f.read()
    f.close()
    return a

def format(a):
    s = a.split('\n')
    for i in range(0, len(s)):
        s[i] = s[i].split(':')
    s.pop()
    print(s)
    return s

def findlist(lista, id):
    for i in lista:
        if i[0] == id:
            print(i[0])
            return i

    return False

print (findlist(format(readfile('Cadastro_Comprador')),'01582842167'))

'''import tkinter as tk
from tkinter import simpledialog


win = tk.Tk()
win.geometry("100x50")

def take_user_input_for_something():
    user_input = simpledialog.askstring("Pop up for user input!", "What do you want to ask the user to input here?")
    if user_input != "":
        print(user_input)

menubar = tk.Menu(win)
dropDown = tk.Menu(menubar, tearoff = 0)
dropDown.add_command(label = "Do something", command = take_user_input_for_something)

# this entry field is not really needed her.
# however I noticed you did not define this widget correctly
# so I put this in to give you an example.
my_entry = tk.Entry(win)
my_entry.pack()

menubar.add_cascade(label = "Drop Down", menu = dropDown)
win.config(menu = menubar)

win.mainloop()'''