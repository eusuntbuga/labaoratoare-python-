def calculeaza_varsta_pisicii():
    print("\n=== Calculator pentru varsta pisicii in ani omenesti ===")
    raspuns = input("Pisica este mai mica de 1 an? (Da/Nu): ").strip().lower()

    if raspuns in ['da', 'yes']:
        pisic_dictionar_luni = {
            1: "6 luni",
            2: "10 luni",
            3: "2 ani",
            4: "5 ani",
            5: "8 ani",
            6: "14 ani",
            7: "15 ani",
            8: "16 ani",
            9: "16 ani",
            10: "17 ani",
            11: "17 ani"
        }

        while True:
            luni_input = input("Introduceti cate luni are pisica (1-11): ")
            try:
                luni = int(luni_input)
            except ValueError as e:
                print(f"Eroare: {e}")
                continue

            if luni not in pisic_dictionar_luni:
                print("Valoarea trebuie sa fie intre 1 si 11.")
                continue

            break

        print(f"In ani omenesti pisica are {pisic_dictionar_luni[luni]}.")

    elif raspuns in ['nu', 'no']:
       
        pisic_dictionar_ani = {
            1: 18,
            2: 25,
            3: 29,
            4: 33,
            5: 37,
            6: 41,
            7: 45,
            8: 49,
            9: 53,
            10: 57,
            11: 61,
            12: 65,
            13: 69,
            14: 73,
            15: 77,
            16: 80,
            17: 83,
            18: 86,
            19: 89,
            20: 92,
            21: 95,
            22: 98,
            23: 101,
            24: 104,
            25: 107,
            26: 110,
            27: 113,
            28: 116,
            29: 119,
            30: 122,
            31: 125,
            32: 128,
            33: 131,
            34: 134
        }

        while True:
            ani_input = input("Cati ani are pisica? (1-34): ")
            try:
                ani = int(ani_input)
            except ValueError as e:
                print(f"Eroare: {e}")
                continue

            if ani not in pisic_dictionar_ani:
                print("Valoarea trebuie sa fie intre 1 si 34.")
                continue

            break

        print(f"In ani omenesti pisica are aproximativ {pisic_dictionar_ani[ani]} ani.")

    else:
        print("Nu ai introdus o opțiune valida. Te rog să scrii 'Da' sau 'Nu'.")

# Rulam programul
calculeaza_varsta_pisicii()
