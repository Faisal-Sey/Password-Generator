
from random import sample, SystemRandom
from string import *
from tkinter import *

root = Tk()
root.title("Random Password Generator")
root.geometry('500x200')
root.configure(bg='brown')


def generator():
    r = SystemRandom()
    u_letters = list(ascii_uppercase)
    l_letters = list(ascii_lowercase)
    key_1 = r.sample(u_letters, 2)
    key_2 = r.sample(l_letters, 2)
    first = r.randint(0, 9)
    second = r.randint(0, 9)
    symbols = ['%', '$', '&', '€', '£', '¥', '~', '|', '}', '{', '-', '^', '<', '>']
    symbols = sample(symbols, 2)
    result = [key_1[0], key_2[1], key_1[1], key_2[0], str(first), str(second), symbols[0], symbols[1]]
    result = r.sample(result, 8)
    password = ''.join(result)
    Label.delete(0, END)
    Label.insert(0, password)


def copy():
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()


def destroy():
    root.destroy()


label = Label(root, text='Password: ', bd=9, bg='brown', fg='white', font='Arial')
label.place(x=70, y=70)
Label = Entry(root, bd=5, bg='brown', font='Arial', fg='white')
Label.place(x=180, y=70)
button1 = Button(root, text='Generate', command=generator, bd=5, bg='brown', fg='white')
button1.place(x=170, y=150)
button2 = Button(root, text='Copy', command=copy, bd=5, bg='brown', fg='white')
button2.place(x=250, y=150)
button3 = Button(root, text='Quit', command=destroy, bd=5, bg='brown', fg='white')
button3.place(x=455, y=165)
root.mainloop()
