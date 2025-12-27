def wydrukujco2(listaliczb:list[int]):
    i=0
    for i in range(0,len(listaliczb),2):
        if i <= len(listaliczb):
            print(listaliczb[i])
        else:
            break

lista_liczb=[715,5,8,95,12,34,78,99,100,1500]
wydrukujco2(lista_liczb)