def cere_int(mesaj):
    while True:
        try:
            valoare = int(input(mesaj))
            return valoare
        except ValueError:
            print("Va rugam sa introduceti un numar intreg valid.")

# Solicitarea varstei utilizatorului
varsta = cere_int("Introduceti varsta dumneavoastra: ")

# Calcularea varstei în 5 ani
varsta_in_5_ani = varsta + 5
print("În 5 ani veti avea " + str(varsta_in_5_ani) + " ani.")
