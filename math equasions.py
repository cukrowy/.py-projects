import random
import time
import os
o = 0
a = int(input("Ile zadań matematycznych:  "))
if a <= 0:
    print('aha')
if a >= 1:
    for i in range(a):
        zadania = random.randint(1, 3) #zmien 3 na 4 jak wymyslisz mnozenie
        if zadania == 1:
            x = random.randint(1, 99)
            y = random.randint(1, 99)
            os.system('clear')
            odp = int(input(f'{x} + {y}?:  '))

            if odp == x + y:
                o = o + 1
                print("Dobra Odpowiedz")
                time.sleep(1)
                os.system('clear')
            else:
                print("Zła Odpowiedź")
                time.sleep(1)
                os.system('clear')
        if zadania == 2:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            os.system('clear')
            odp = int(input(f'{x} x {y}?:  '))

            if odp == x * y:
                o = o + 1
                print("Dobra Odpowiedz")
                time.sleep(1)
                os.system('clear')
            else:
                print("Zła Odpowiedź")
                time.sleep(1)
                os.system('clear')
        if zadania == 3:
             x = random.randint(1, 100)
             y = random.randint(1, 100)
             os.system('clear')
             odp = int(input(f'{x} - {y}?:  '))

             if odp == x - y:
                 o = o + 1
                 print("Dobra Odpowiedz")
                 time.sleep(1)
                 os.system('clear')
             else:
                 print("Zła Odpowiedź")
                 time.sleep(1)
                 os.system('clear')
        #if zadania == 4:
             #x = random.randint(1, 100)
             #y = random.randint(1, 10)
             #os.system('clear')
             #odp = int(input(f'{x} : {y}?:  '))

             #if odp == x / y:
                 #o = o + 1
                 #print("Dobra Odpowiedz")
                 #time.sleep(1)
                 #os.system('clear')
             #else:
                 #print("Zła Odpowiedź")
                 #time.sleep(1)
                 #os.system('clear')
            
time.sleep(0)
if a >= 1:
    print(f'{o} dobrych odpowiedzi z {a}')
    time.sleep(1)
    input("\n\nNaciśnij enter aby wyjść")
else:
    time.sleep(1)
    input("\n\nNaciśnij enter aby wyjść")
