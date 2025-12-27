def czyparzysta(x:int):
    if x % 2 == 0:
        return True
    else:
        return False

x=5
print('Przypadek liczby podanej do funkcji: ',x)
x_check = czyparzysta(x)
if x_check:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')

y=6
print('Przypadek liczby podanej do funkcji: ',y)
y_check = czyparzysta(y)
if y_check:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')