def aduna_cu_fiecare(numar_dat, lista):
    x = range(len(lista))
    for n in x:
        list = lista[n] + numar_dat
        lista[n] = list
    print(list)

numar_dat = 5
lista = [1, 2, 3, 4,]
aduna_cu_fiecare(numar_dat, lista)
print(lista)



