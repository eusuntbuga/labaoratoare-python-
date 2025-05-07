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
        # Generare dictionar pentru varsta pisicii in ani omenesti
        pisic_dictionar_ani = {}

        for i in range(1, 35):
            if i == 1:
                pisic_dictionar_ani[i] = 18
            elif i == 2:
                pisic_dictionar_ani[i] = 25
            elif i <= 15:
                pisic_dictionar_ani[i] = pisic_dictionar_ani[i - 1] + 4
            else:
                pisic_dictionar_ani[i] = pisic_dictionar_ani[i - 1] + 3

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
        print("Nu ai introdus o optiune valida. Te rog sa scrii 'Da' sau 'Nu'.")

# Rulam programul
calculeaza_varsta_pisicii()
