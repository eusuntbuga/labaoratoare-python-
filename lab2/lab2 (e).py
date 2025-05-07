# Dictionar bazat pe chei de tip text
dict_text = {"produs_1": "Mere", "produs_2": "Banane", "produs_3": "Pere"}
# Dictionar bazat pe chei numerice
dict_numeric = {1: "Mere", 2: "Banane", 3: "Pere"}

# Afisarea unui element din fiecare dicționar
print("Un element din dicționarul text:", dict_text["produs_1"])
print("Un element din dicționarul numeric:", dict_numeric[2])

# Manipularea dictionarelor
dict_text["produs_4"] = "Struguri"  # Adaugarea unui element
dict_numeric[4] = "Capsuni"
print("Dictionarul text după adaugare:", dict_text)
print("Dictionarul numeric după adaugare:", dict_numeric)

# Functii aplicate dicționarului
print("Cheile dictionarului text:", dict_text.keys())  # Functie: cheile dictionarului
print("Valorile dictionarului numeric:", dict_numeric.values())  # Functie: valorile dictionarului


