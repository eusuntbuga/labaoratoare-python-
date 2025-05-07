

# 1) Explicați ce a fost realizat în următorul exemplu:
# Se creează o funcție lambda care salută utilizatorul cu numele introdus

greet_user = lambda name: print('Hello My Dear,', name)
user_name = input("What is your name? ")
greet_user(user_name)

print("\n-----------------------------\n")

# 2) Sortați o listă de 7 tupluri a câte 2 elemente, după cel de-al doilea element
# Se folosește sorted() cu o funcție lambda pentru a sorta tuplurile după al doilea element (x[1])

lista = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 10), (2, 4)]
lista_sortata = sorted(lista, key=lambda x: x[1])
print("Lista sortata după al doilea element:")
print(lista_sortata)

print("\n-----------------------------\n")

# 3) Creați propria funcție-lambda pentru a rezolva o problemă
# Exemplu: dublăm un număr

dubleaza = lambda x: x * 2
numar = 6
print("Dublul numarului", numar, "este:", dubleaza(numar))

# Explicație: funcția primește un număr și returnează dublul său

print("\n-----------------------------\n")

# 4) Definiți câte o funcție de următoarele tipuri:

# a. Fără parametri
def salut():
    print("Salut! Eu sunt o functie fara parametri.")

# Cu parametri
def afiseaza_nume(nume):
    print("Numele tau este:", nume)

# Cu valori predefinite pentru parametri
def saluta_persoana(nume="Anton"):
    print("Buna,", nume)

# b. Care returnează un rezultat
def inmulteste(a, b):
    return a * b

# Care nu folosește return
def afiseaza_mesaj():
    print("Aceasta este o functie care nu returneaza nimic.")

print("Apeluri functii:\n")
salut()
afiseaza_nume("Ion")
saluta_persoana()
saluta_persoana("Maria")

rezultat = inmulteste(3, 4)
print("Rezultatul inmultirii este:", rezultat)

afiseaza_mesaj()

# 5) Apelați funcțiile pentru a rezolva unele probleme și explicați
# Fiecare funcție este apelată în funcție de modul în care a fost definită:
# - fără parametri => cu paranteze ()
# - cu parametri => se transmit valorile
# - cu return => salvăm rezultatul într-o variabilă
# - fără return => doar afișăm ceva
