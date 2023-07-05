#1 ПРИМЕР
# Типы данных
'''
# 1 -> string- str()- это все что связано с текстами, буквами, словами
# как мы знаем с str нельзя прибавлять или отнимать можно только умножать
#Пример
print(type('Hello World'))

#2 -> integer - int() - это все что связано с целыми числами. Пример:
print(type(11231))

#3 -> float - float() - это как мы знаем дробные числа. Пример:
print(type(1.125))

#4 -> boolean - bool() - это у нас логические данные, которая дает нам результат True or False. Пример
print(type(True))
'''
#2 ПРИМЕР
'''a = ((23+17)/2)%5
# 23 + 17 = 40 делим на 2 = 20 , так как мы использовали деление с остатком(%) получается 0
print(a)
'''
#3 ПРИМЕР
'''print('Hello') # выводит нам результат на экран
#return -> это используется в функциях, оно запускает результат но не выводит на экран
'''
#4 ПРИМЕР
'''number = 25
a = 25//10 #нашел 1ую цифру
b = 25%10 #нашел 2ую цифру
print(a+b)
'''
#5 ПРИМЕР
'''num1 = int(input('Enter your number: '))
num2 = int(input('Enter 2nd your number: '))
if num1 > num2:
    print(f'{num1} число больше {num2}')
elif num2 > num2:
    print(f'{num2} число больше {num2}')
else:
    print('Ошибка')
'''
#6ПРИМЕР
'''for i in range(1500,2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
   
'''
#7ПРИМЕР
'''for i in range(0,7):
    if i == 3:
        continue
    elif i == 6:
        continue
    print(i)'''
#8ПРИМЕР
'''text = 'Im a beginner\n'
print(10*text)
'''
#9ПРИМЕР
'''for i in range(1,21):
    if i % 2 == 0:
        print(i,end=',')
print('=Четные')
for i in range(1, 21):
    if i % 2 == 1:
        print(i,end=',')
print('=Нечетные')
'''
#10ПРИМЕР
'''tot = 0
for i in range(1,21):
    if i >= 5 and i <= 15:
        tot += i
        print(i)
print(f'Сумма цифр равна = {tot}')
'''
#11ПРИМЕР
'''i = 0
tot = 0
for i in range(0,10):
    i += 1
    i /= 10
    tot += 10
    print(i,f'{tot} кг')
'''
#12ПРИМЕР
'''i = 1
fact = 1
while i<10:
    i+= 1
    fact = fact*i
    print(i,end='->')
    print(fact)
'''
#13ПРИМЕР
'''lst = [1,'hello',1.42,True,'red']
print(lst)
lst.insert(0,3)
print(f'К листу добавился число 3 с индексом 0 = {lst}')
'''
#14ПРИМЕР
'''from random import randint
nums = [randint(1,10) for i in range(randint(5,10))]
print(nums)
print(sum(nums))
'''
#15ПРИМЕР
'''from random import randint
nums = [randint(1,100) for i in range(randint(5,10))]
print(nums)
print(f'Минимальное число = {min(nums)}')
print(f'Максимальное число = {max(nums)}')
'''
#16ПРИМЕР
'''from random import randint
nums = [randint(1,10) for i in range(randint(0,3))]
print(nums)
if len(nums) == 0:
    print('Лист пуст!!!')
elif len(nums) >= 1:
    print('В листе есть данные')
else:
    print('Ошибка')
'''
#17ПРИМЕР
'''kort = ('red','yellow')
print(kort)
for kor in kort:
    for i in kor:
        print(i, end='')
'''
#18ПРИМЕР
'''dict = {
    'nums': 1234,
    'alpha': 'abscd'
}
for k,v in dict.items():
    print(f'{k}:{v}')
a = input('Enter your key: ')
if a in dict.keys():
    print('Yesss')
else:
    print('Wrong')
'''
#19ПРИМЕР
'''from random import randint
nums = {randint(1,10) for i in range(randint(0,10))}
print(nums)
print(type(nums))
'''
#20ПРИМЕР
'''from random import randint
nums = [randint(1,10) for i in range(randint(4,5))]
print(nums)
def MAX2(A,B):
    return
A = max(nums)
B = min(nums)
print(A,B)
'''
#21ПРИМЕР НЕРЕШЕНО
'''from random import randint
nums = [randint(1,10) for i in range(randint(5,10))]
print(nums)
def tot(i):
    pass
'''
#22ПРИМЕР НЕРЕШЕНО
'''lst = ['Aziz','Jamshid','Begzod']
print(lst)
def student(lst):
    pass
'''
#24ПРИМЕР
'''import tkinter

screen = tkinter.Tk()
screen.title('24-task')
screen.geometry('800x600')
screen.resizable(width=False,height=False)
screen.configure(background='yellow')

Label = tkinter.Label(
    screen,
    text='Python:)',
    width=50,
    bg= 'red'
)
Label.place(x=50,y=50)

screen.mainloop()
'''
#25ПРИМЕР
'''
import tkinter

screen = tkinter.Tk()
screen.title('25-task')
screen.geometry('800x600')
screen.resizable(width=False,height=False)
screen.configure(background='#CCFFCC')

intro = tkinter.Label(
    screen,
    text='Last App',
    font='Carrington 15',
    fg='black',
    bg='red'
)
intro.pack(anchor='center')

Label = tkinter.Label(
    screen,
    text='Python:)',
    width=50,
    bg= 'red'
)
Label.pack(anchor='center')

screen.mainloop()'''