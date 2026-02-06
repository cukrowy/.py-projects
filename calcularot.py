import time
import os
while True:
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    pytanie = int(input("jaki typ obliczenia    "))
    if pytanie == 1:
        print("  ")
        def sum(a, b):
            return (a + b)

        a = int(input('Podaj pierwszą liczbe:  '))
        print("  ")
        b = int(input('Podaj drugą liczbe:  '))
    elif pytanie == 2:
        def sum(a, b):
            return (a - b)
    
        a = int(input('Podaj pierwszą liczbe:  '))
        print("  ")
        b = int(input('Podaj drugą liczbe:  '))
        
    elif pytanie == 3:
        def sum(a, b):
            return (a * b)
        
        a = int(input('Podaj pierwszą liczbe:  '))
        print("  ")
        b = int(input('Podaj drugą liczbe:  '))
    elif pytanie == 4:
        def sum(a, b):
            return (a / b)
    
        a = int(input('Podaj pierwszą liczbe:  '))
        print("  ")
        b = int(input('Podaj drugą liczbe:  '))
    print("  ")
    print(f'Twój wynik to {sum(a, b)}')
    time.sleep(1)
    os.system('cls')
    time.sleep(0)
  