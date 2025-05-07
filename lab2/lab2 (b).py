# Definirea unei liste
lista = [10, 20, 30, 40, 50]

# Afisarea primei și a treia valori
print("Prima valoare din listă:", lista[0])
print("A treia valoare din listă:", lista[2])

# Inlocuirea unei valori din lista
lista[2] = 100
print("Lista după inlocuire:", lista)

# Extractie de elemente din lista
sub_lista = lista[1:4]  
print("Sublista extrasa:", sub_lista)

# Aplicarea de metode, functii și operatori
lista.append(60)
print("Lista după adaugare:", lista)

lungime_lista = len(lista)
print("Lungimea listei:", lungime_lista)

suma_lista = sum(lista)
print("Suma elementelor din lista:", suma_lista)

lista.sort()
print("Lista sortata:", lista)


