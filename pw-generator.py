from ast import Break
import string
import random

from regex import W



def passwd1():
    pw1 = string.ascii_letters
    print(''.join(random.choice(pw1)for i in range(5)))


def passwd2():
    pw2 = string.ascii_letters
    print(''.join(random.choice(pw2) for i in range(12)))

def passwd3():
    pw3 = string.ascii_letters
    print(''.join(random.choice(pw3) for i in range(20)))

def passwd4():
    pw4 = string.ascii_letters
    print(''.join(random.choice(pw4)for i in range(35)))



def options():
    print("""
                The options - 
            1. 5 length
            2. 12 length
            3. 20 length
            4. 35 length
            To exit press Q to exit
            """)
options()
def ask():
    
    while True:       
        user = input ("Choose: ")
        if (user == '1'):
            passwd1()
        elif (user == '2'):
            passwd2()
        elif (user == '3'):
            passwd3()
        elif (user == '4'):
            passwd4()
        elif (user == 'Q' or 'q'):
            break
        else:
            print("You didnt choose anything")
ask()












