def czyparzysta(listaliczb:list[int]):
    return (x for x in listaliczb if x % 2 == 0)

lista_liczb=[1,2,3,4,5,8,6,11,15,236]
lista2=range(1,11)
rezultat = czyparzysta(lista_liczb)
for x in rezultat:
    print(x)
rezultat2=czyparzysta(lista2)
for x in rezultat2:
    print(x)