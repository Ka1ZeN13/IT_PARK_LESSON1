import tkinter
from pathlib import Path
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk

screen = tkinter.Tk()
screen.title('My 1st mini-app')
screen.geometry('800x600')
screen.resizable(width=False,height=False)
screen.configure(background='yellow')

def operation():
    text = int(field_1.get())
    text1 = int(field_2.get())
    return messagebox.showinfo(title='Result', message=f'{text+text1}')
def clean():
    text = field_1.delete(first=0, last=tkinter.END)
    text1 = field_2.delete(first=0, last=tkinter.END)
    return text
    return text1

intro = tkinter.Label(
    screen,
    text='First app',
    font='Carrington 15',
    fg='black',
    bg='red'
)
intro.pack(anchor='center')

a = ttk.Label(
    screen,
    text='a:',
    font='Carrongton 15',
    fg= 'black',
    bg= 'yellow'
)
a.place(x=20,y=68)

b = ttk.Label(
    screen,
    text='b:',
    font='Carrongton 15',
    fg= 'black',
    bg= 'yellow'
)
b.place(x=20,y=120)

field_1 = ttk.Entry(
    screen,
    width=30

)
field_1.focus()
field_1.place(x=50, y=75)

field_2 = ttk.Entry(
    screen,
    width=30
)
field_2.place(x=50, y=125)

press = ttk.Button(
    screen,
    text='Press',
    fg='black',
    bg='#34eb5b',
    command=operation
)
press.place(x=250, y=70)

remove = ttk.Button(
    screen,
    text='Clean',
    fg='white',
    bg='#eb3434',
    command=clean,
    width=15

)
remove.place(x=250, y=120)

if __name__ == '__main__':
    #screen.config(menu=menubar)
    screen.mainloop()
