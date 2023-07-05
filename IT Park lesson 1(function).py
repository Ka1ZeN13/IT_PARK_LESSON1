'''
def func():
    print('Hello')
func()

def name():
    print('Ka1zen')
name()

def FI(A,B):
    print(A, B)

A = 'Aziz'
B = 'Ka1zen'
FI(A, B)

def translate(A):
    return A.lower()
print(A)
A = translate(A)
print(A)

'''

'''def proc():
    a = int(input('Number: '))
    b = int(input('Number: '))
    print(a+b)


def sub():
    a = int(input('Number: '))
    b = int(input('Number: '))
    print(a-b)


def multip():
    a = int(input('Number: '))
    b = int(input('Number: '))
    print(a*b)


def divide():
    a = int(input('Number: '))
    b = int(input('Number: '))
    print(a/b)


proc()
sub()
multip()
divide()'''

'''def name(name):
    print(name)
name('Aziz')

def FI(name,fam):
    print(name,fam)

FI('Aziz','Djumaniyazov')

from random import randint

def plus(a,b):
    print(a+b)
print('Plus -->',end=' ')
plus(randint(1,20),randint(20,40))

def minus(a,b):
    print(a-b)

print('Minus -->',end=' ')
minus(randint(15,30),randint(1,15))

def multi(a,b):
    print(a*b)

print('Multiple -->',end=' ')
multi(randint(15,30),randint(1,15))

def div(a,b):
    print(a/b)

print('Divide -->',end=' ')
div(randint(15,30),randint(1,15))


def qosiw(a,b):
    print(a+b)

qosiw(int(input('a:')),int(input('b:')))'''

#
# def func():
#     user = int(input('Enter your number: '))
#     if user >= 18:
#         print('Congratulations')
#     else:
#         print('Opps,sorry')
# func()


# def func():
#     user_age = int(input('Enter your number: '))
#     while user_age != 21:
#         user_age = int(input('Enter your number: '))
#     if user_age == 21:
#         print(f'Your age: {2023-user_age}')
#     else:
#         print('Your are too small!!!')
# func()

def func():
    user = []
    user.append('Aziz')
    user.append('Darman')
    user.append('Rafat')
    user.append('Djamshid')
    user.append('Gozzal')
    print(len(user))
    print(user)
    print(sorted(user))

func()
