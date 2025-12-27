def iloczynliczb(listaliczb:list[int]):
    i=0
    for i in range(0,5):
        print(listaliczb[i]*2)

def iloczynliczbLS(listaliczb:list[int]):
    return (x*2 for x in listaliczb)

lista_liczb=[1,2,3,4,5]
iloczynliczb(lista_liczb)
rezultat = iloczynliczbLS(lista_liczb)
for x in rezultat:
    print(x)