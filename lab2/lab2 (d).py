# Definirea unui set cu elemente duplicate
set_1 = {10, 20, 20, 30, 30, 30}

# Afisarea elementelor setului
print("Elementele setului:", set_1)

# Setul nu permite duplicate, așa că elimină valorile repetate.
# Aplicati o metodă și o funcție
set_1.add(40)  # Metoda: adăugarea unui element
print("Setul după adăugare:", set_1)

set_1_remove = set_1.pop()  # Functie: eliminarea unui element 
print("Elementul eliminat aleatoriu din set:", set_1_remove)
print("Setul după eliminare:", set_1)

#Deasemeanea putem folosi set.remove(element)