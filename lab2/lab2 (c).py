# Definirea unui tuplu
tuplu = (1, 2, 3, 4, 5)

# Tiparirea tipului de date al tuplului
print("Tipul tuplului:", type(tuplu))

# Afisarea primei și ultimei valori
print("Prima valoare din tuplu:", tuplu[0])
print("Ultima valoare din tuplu:", tuplu[-1])

# Extractie de date din tuplu
sub_tuplu = tuplu[1:4]
print("Subtuplu extrase:", sub_tuplu)

# Functii aplicate tuplului
tuplu_lungime = len(tuplu)  # Functie: lungimea tuplului
print("Lungimea tuplului:", tuplu_lungime)

tuplu_maxim = max(tuplu)  # Functie: valoarea maximă
print("Valoarea maximă din tuplu:", tuplu_maxim)

tuplu_suma = sum(tuplu)  # Functie: suma elementelor
print("Suma elementelor din tuplu:", tuplu_suma)
