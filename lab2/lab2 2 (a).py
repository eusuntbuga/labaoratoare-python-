# Listă cu preturi si denumiri de produse
#produse = ["Mere", "Banane", "Pere"]
#preturi = [2.5, 3.0, 1.8]

# Crearea unui șablon cu metoda format()
#for i in range(len(produse)):
#    print("Produs: {} - Preț: {} lei".format(produse[i], preturi[i]))




# Lista cu preturi si denumiri de produse
produse = ["Mere", "Banane", "Pere"]
preturi = [2.5, 3.0, 1.8]

# Adaugare de produse si preturi de la utilizator
while True:
    optiune = input("Vrei să adaugi un produs? (da/nu): ").strip().lower()
    if optiune == "nu":
        break
    elif optiune == "da":
        produs_nou = input("Introduceti numele produsului: ")

        while True:
            try:
                pret_nou = float(input("Introduceti prețul produsului: "))
                break
            except ValueError:
                print("Pretul trebuie să fie un numar!")
                continue
        
        produse.append(produs_nou)  # Adaugare produs in lista
        preturi.append(pret_nou)    # Adaugare pret in lista
    else:
        print("Optiune invalida! Raspundeti cu 'da' sau 'nu'.")

# Afisarea listei complete de produse si preturi
print("\nLista finala de produse si preturi:")
for i in range(len(produse)):
    print(f"Produs: {produse[i]} - Pret: {preturi[i]} lei")






