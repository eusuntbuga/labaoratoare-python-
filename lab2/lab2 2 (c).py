# Verificarea prezenței unui element într-o listă
#fructe = ["măr", "banană", "para"]
#print(fructe)
#print("Banana este în listă?", "banană" in fructe)  # True
#print("Struguri sunt în listă?", "struguri" not in fructe)  # True

# Adăugarea unui nou fruct
#fruct_nou = input("Introduceți un fruct de adăugat: ")
#fructe.append(fruct_nou)  # Adaugam noul fruct în listă
#print("Lista actualizata:", fructe)

# Lista de masini
#masini = ["Audi", "BMW", "Lexus", "Ford"]
#print(masini)
#print("Audi este în listă?", "Audi" in masini)  # True
#print("Toyota este în listă?", "Toyota" in masini)  # False





masini = []
carburant = []

while True:
    optiune = input("Doresti sa adaugi o masina noua (da/nu): ").strip().lower()
    
    if optiune == "nu":
        break
    elif optiune == "da":
        masina_noua = input("Introduceti marca automobilului: ").strip()
        carburant_nou = input("Introduceti carburantul automobilului: ").strip()
        
        masini.append(masina_noua)
        carburant.append(carburant_nou)
    else:
        print("Optiune invalida, alegeti 'da' sau 'nu'.")

# Afisarea listei finale
print("\nLista finala:")
for i in range(len(masini)):
    print(f"Masina: {masini[i]} - Carburant: {carburant[i]}")






