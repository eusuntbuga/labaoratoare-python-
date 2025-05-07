def calculeaza_greutatea_ideala():
    print("=== Calculator pentru greutatea ideala (formula Lorentz) ===")
    while True:
        i = input("Introduceti inaltimea (cm): ")

        try:
            inaltime = int(i)
        except ValueError as e:
            print(f"Eroare: {e}")
            continue

        if not 150 <= inaltime <= 220:
            print("Inaltimea trebuie sa fie intre 150 si 220 cm.")
            continue

        break

    while True:
        a = input("Introduceti greutatea actuala (kg):")

        try:
            greutate = float(a)
        except ValueError as e:
            print(f"Eroare: {e}")
            continue

           
        if not 45 <= greutate <= 300:
            print("Greutatea trebuie sa fie intre 45 si 300 kg.")
            continue
    
        break
        

    while True:
        try:
            varsta = int(input("Introduceti varsta (ani): "))
            if not 21 <= varsta < 120:
                raise ValueError("Varsta trebuie sa fie intre 21 si 119 ani.")
            break
        except ValueError as e:
            print(f"Eroare: {e}")

    while True:
        sex = input("Introduceti sexul (M/F): ").strip().upper()
        if sex not in ['M', 'F']:
            print("Valoare invalida. Introduceti doar 'M' sau 'F'.")
        else:
            break

    if sex == 'M':
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 4 + (varsta - 20) / 4)
    else:  # F
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 2.5 + (varsta - 20) / 6)

    print(f"\nGreutatea ideala calculata este: {greutate_ideala:.2f} kg")

    diferenta = greutate - greutate_ideala
    if diferenta > 0:
        print("Recomandare: Ar trebui sa slabiti putin.")
    else:
        print("Recomandare: Ar trebui sa adaugati in greutate.")

def calculeaza_varsta_pisicii():
    print("\n=== Calculator pentru varsta pisicii in ani omenesti ===")
    raspuns = input("Pisica este mai mica de 1 an? (Da/Nu): ").strip().lower()

    if raspuns in ['da', 'yes']:
        pisic_dictionar = {
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
            try:
                luni = int(input("Introduceti cate luni are pisica (1-11): "))
                if luni not in pisic_dictionar:
                    raise ValueError("Valoarea trebuie sa fie intre 1 si 11.")
                break
            except ValueError as e:
                print(f"Eroare: {e}")
        print(f"In ani omenesti pisicul are {pisic_dictionar[luni]}.")
    else:
        while True:
            ani_input = input("Cati ani are pisica? (1-35): ")
            if not ani_input.isdigit():
                print("Introduceti un numar valid.")
                continue
            ani = int(ani_input)
            if not 1 <= ani < 35:
                print("Valoarea trebuie sa fie intre 1 si 34.")
                continue
            break

        if ani == 1:
            om_ani = 18
        elif ani == 2:
            om_ani = 25
        elif 3 <= ani <= 15:
            om_ani = 25 + (ani - 2) * 4
        else:
            om_ani = 25 + (13 * 4) + (ani - 15) * 3

        print(f"In ani omenesti pisica are aproximativ {om_ani} ani.")

# Rulam programul
calculeaza_greutatea_ideala()
calculeaza_varsta_pisicii()
