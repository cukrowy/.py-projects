import random
import time
import os
o = 0
a = int(input("Ile zadań matematycznych:  "))
 
for i in range(a):
    x = random.randint(1, 99)
    y = random.randint(1, 99)

    odp = int(input(f'{x} + {y}?:  '))

    if odp == x + y:
        o = o + 1
        print("dobra odpowiedz")
        time.sleep(1)
        os.system('cls')
    else:
        print("źle")
        time.sleep(1)
        os.system('cls')
time.sleep(0)
print(f'{o} dobrych odpowiedzi z {a}')
time.sleep(1)
input("\n\nNaciśnij enter aby wyjść")