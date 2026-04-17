
N = 5
a = [0] * N
def wprowadz_dane():
    for i in range(N):
        a[i] = int(input("podaj liczbe: "))
def wyprowadz_dane():
    for i in range(N):
        print(a[i])

def wyszukaj_dana(wartosc):
    for i in range(N):
        if a[i] == wartosc:
            return i
    return -1
    
wprowadz_dane()

print("Wprowadzone dane:")
wyprowadz_dane()
wartosc = int(input("Podaj daną do wyszukiwania: "))
pozycja = wyszukaj_dana(wartosc)
if pozycja >= 0:
    print("znaleziono daną", wartosc, "na pozycji", pozycja)
    print("pozycje liczone sa od zera")
else:
    print("nie znaleziono danej", wartosc)
    
input("\n\nNacisnij enter, aby zakonczyc")
    
    
