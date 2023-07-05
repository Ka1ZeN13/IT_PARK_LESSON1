'''#Class work
import tkinter
from pathlib import Path
from tkinter import messagebox
from tkinter import Menu

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

a = tkinter.Label(
    screen,
    text='a:',
    font='Carrongton 15',
    fg= 'black',
    bg= 'yellow'
)
a.place(x=20,y=68)

b = tkinter.Label(
    screen,
    text='b:',
    font='Carrongton 15',
    fg= 'black',
    bg= 'yellow'
)
b.place(x=20,y=120)

field_1 = tkinter.Entry(
    screen,
    width=30

)
field_1.focus()
field_1.place(x=50, y=75)

field_2 = tkinter.Entry(
    screen,
    width=30
)
field_2.place(x=50, y=125)

press = tkinter.Button(
    screen,
    text='Press',
    fg='black',
    bg='#34eb5b',
    command=operation
)
press.place(x=250, y=70)

remove = tkinter.Button(
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
'''
#1
'''import tkinter
from tkinter import messagebox

screen = tkinter.Tk()
screen.title('My 1st mini-app')
screen.geometry('800x600')
screen.resizable(width=False,height=False)
screen.configure(background='green')

def hello():
    text = field_1.get()
    return messagebox.showinfo(title='Result',
    message=f'Hello {text}!!!')

field_1 = tkinter.Entry(
    screen,
    width=30
)
press = tkinter.Button(
    screen,
    text='Press',
    fg='black',
    bg='red',
    command=hello
)
press.place(x=250, y=70)

field_1.focus()
field_1.place(x=50, y=75)

if __name__ == '__main__':
    screen.mainloop()
'''

#2
'''import tkinter
import random

screen = tkinter.Tk()
screen.title('My 1st mini-app')
screen.geometry('800x600')
screen.resizable(width=False,height=False)
screen.configure(background='yellow')


def roll_dice():
    number = random.randint(1, 6)
    label.config(text=f"Выпало число: {number}")

button = tkinter.Button(
    screen,
    fg='black',
    bg='#34eb5b',
    width=30,
    text="Бросить кости",
    command=roll_dice
)
button.place(x=250, y=70)

label = tkinter.Label(
    screen,
    fg='green',
    bg='red',
    width=30,
    text=""
)
label.place(x=250 , y = 100)

screen.mainloop()
'''
#3
'''import tkinter

# Окно
screen = tkinter.Tk()
screen.title('First app')
screen.configure(background='#CCFFCC')
screen.geometry('1024x780')
screen.resizable(width=False, height=False)

total = 0

def total1():
    global total
    number = int(field_1.get())
    total += number
    label.config(text=f"Общий результат: {total}")
def clean():
    global total
    total = 0
    label.config(text="")

intro = tkinter.Label(
    screen,
    text='Third programm',
    font='Roboto 10',
    fg='white',
    bg='red'
)
intro.pack(anchor='center')

field_1 = tkinter.Entry(
    screen,
    width=20
)
field_1.focus()
field_1.place(x=20, y=75)
press = tkinter.Button(
    screen,
    text='Add',
    fg='white',
    bg='#34eb5b',
    command=total1
)
press.place(x=20, y=110)

remove = tkinter.Button(
    screen,
    text='Remove',
    fg='white',
    bg='#eb3434',
    command=clean
)
remove.place(x=70, y=110)
label = tkinter.Label(
    screen,
    fg='green',
    bg='red',
    width=30,
    text="",
)
label.place(x=150 , y = 75)

screen.mainloop()
'''
#4
'''import tkinter

# Окно
screen = tkinter.Tk()
screen.title('First app')
screen.configure(background='#CCFFCC')
screen.geometry('1024x780')
screen.resizable(width=False, height=False)


def add_name():
    name = name_entry.get()
    if name:
        names_list.append(name)
        update_names()

def clear_names():
    global names_list
    names_list = []
    update_names()

def update_names():
    names_text = "\n".join(names_list)
    names_label.config(text=names_text)

names_list = []



name_label = tkinter.Label(
    screen,
    text="Введите имя:")

name_label.pack()

name_entry = tkinter.Entry(screen)
name_entry.pack()

add_button = tkinter.Button(
    screen,
    text="Добавить",
    fg='white',
    bg='#34eb5b',
    command=add_name)
add_button.pack()

names_label = tkinter.Label(
    screen,
    text="")
names_label.pack()

clear_button = tkinter.Button(
    screen,
    text="Очистить список",
    fg='white',
    bg='#eb3434',
    command=clear_names)
clear_button.pack()

screen.mainloop()'''
#5
'''import tkinter


screen = tkinter.Tk()
screen.title('First app')
screen.configure(background='#CCFFCC')
screen.geometry('1024x780')


def convert():
    miles = float(entry.get())
    kilometers = miles * 1.6093
    result_label.config(text=f'{miles} миль = {kilometers} километров')

label = tkinter.Label(
    screen,
    text="Введите количество миль:",
    background='#4fed11'
)
label.place(x=80, y=50)

entry = tkinter.Entry(screen)
entry.place(x=80, y=75)

button = tkinter.Button(
    screen,
    text="Конвертировать",
    background='#f7485c',
    command=convert
)
button.place(x=80, y=100)

result_label = tkinter.Label(
    screen,
    text="",
    background='#eded11'
)
result_label.place(x=250, y=75)

screen.mainloop()
'''
#6
'''import tkinter
from tkinter import messagebox

screen = tkinter.Tk()
screen.geometry('1024x780')
screen.configure(background='#CCFFCC')
screen.resizable(width=False, height=False)
screen.title("Список чисел")


def add_number():
    number = entry.get()
    if number.isdigit():
        number_listbox.insert(tkinter.END, int(number))
        entry.delete(0, tkinter.END)
    else:
        entry.delete(0, tkinter.END)
        messagebox.showerror("Ошибка", "Введите целое число")

def clear_list():
    number_listbox.delete(0, tkinter.END)


frame = tkinter.Frame(screen)
frame.place(x=50, y=120)

label = tkinter.Label(
    screen,
    background='#eded11',
    text="Введите целое число:")
label.place(x=50, y=140)

entry = tkinter.Entry(
    screen,
    background='#bbfcf5'
)
entry.place(x=50, y=160)

add_button = tkinter.Button(
    screen,
    text="Добавить",
    background='#8fffa5',
    command=add_number)
add_button.place(x=50, y=180)

number_listbox = tkinter.Listbox(
    screen,
    background='#eded11'
)
number_listbox.place(x=50,y=200)

clear_button = tkinter.Button(
    screen,
    text="Очистить список",
    background='red',
    command=clear_list)
clear_button.place(x=50,y=390)

screen.mainloop()'''
#7
'''
import tkinter
from tkinter import messagebox
import csv

screen = tkinter.Tk()
screen.geometry('1024x780')
screen.configure(background='#CCFFCC')
screen.resizable(width=False, height=False)
screen.title("Список чисел")


def add_number():
    number = entry.get()
    if number.isdigit():
        number_listbox.insert(tkinter.END, int(number))
        entry.delete(0, tkinter.END)
    else:
        entry.delete(0, tkinter.END)
        messagebox.showerror("Ошибка", "Введите целое число")

def clear_list():
    number_listbox.delete(0, tkinter.END)

def save_list():
    tmp_list = number_listbox.get(0, tkinter.END)
    with open('numbers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Numbers"])
        for num in tmp_list:
            writer.writerow([num])
            
frame = tkinter.Frame(screen)
frame.place(x=50, y=120)

label = tkinter.Label(
    screen,
    background='#eded11',
    text="Введите целое число:")
label.place(x=50, y=140)

entry = tkinter.Entry(
    screen,
    background='#bbfcf5'
)
entry.place(x=50, y=160)

add_button = tkinter.Button(
    screen,
    text="Добавить",
    background='#8fffa5',
    command=add_number)
add_button.place(x=50, y=180)

number_listbox = tkinter.Listbox(
    screen,
    background='#eded11'
)
number_listbox.place(x=50,y=200)

clear_button = tkinter.Button(
    screen,
    text="Очистить список",
    background='red',
    command=clear_list)
clear_button.place(x=50,y=390)
save_button = tkinter.Button(
    screen,
    text="Сохранить в файл",
    background='blue',
    command=save_list)
save_button.place(x=50,y=420)

screen.mainloop()'''
#8
import tkinter
import csv
from tkinter import messagebox


mainlst = []

screen = tkinter.Tk()
screen.title('Создать csv файл')
screen.geometry('800x600')
screen.configure(background='#CCFFCC')
screen.resizable(width=False, height=False)

def create():
    with open('file.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        messagebox.showinfo(title='Инфо', message='Файл успешно создан')

def save():
    lst = [entry.get(), entry2.get()]
    mainlst.append(lst)
    with open("file.csv","w") as file:
      writer = csv.writer(file)
      writer.writerow(["Name","Age"])
      writer.writerows(mainlst)
      messagebox.showinfo("Инфо","Успешно сохранено")

entry = tkinter.Entry(
    screen
)
entry.place(x=50,y=50)

entry2 = tkinter.Entry(
    screen
)
entry2.place(x=50,y=75)


button = tkinter.Button(
    screen,
    width=15,
    text='Создать файл',
    background='#34e5eb',
    command=create
)
button.place(x=50,y=100)

button2 = tkinter.Button(
    screen,
    width=15,
    text='Сохранить данные',
    background='#34e5eb',
    command=save
)
button2.place(x=50,y=130)

screen.mainloop()


