#8
import tkinter
import csv
from tkinter import messagebox
from tkinter import ttk
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
    with open("file.csv", "w", newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Name","Age"])
      writer.writerows(mainlst)
      messagebox.showinfo("Инфо","Успешно сохранено")

def show():
    with open("file.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


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

button2 = ttk.Button(
    screen,
    width=15,
    text='Сохранить данные',
    background='#34e5eb',
    command=save
)
button2.place(x=50,y=130)

show_button = ttk.Button(
    screen,
    width=15,
    text='Показать данные',
    background='orange',
    command=show
)
show_button.place(x=50,y=150)

screen.mainloop()
