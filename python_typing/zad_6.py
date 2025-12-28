def scallisty(lista1: list[int], lista2: list[int]):
    unikalnalista = list(set(lista1+lista2))
    return [x**3 for x in unikalnalista]


print(scallisty([3, 2, 4], [1, 2, 5]))
