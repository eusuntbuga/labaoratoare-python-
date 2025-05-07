#Afișați un mesaj de salut pe ecran, folosind funcțiile print() și input(),


nume = input("Introduceti numele dumneavoastra: ")
print(f"Salut, {nume}!")

#Definiți 4 variabile, folosind denumiri corecte pentru ele în Python.

var_int = 42
var_string = "BMW"
var_text_scurt = "Salut"
var_text_lung = """ion este 
jucator de 
pubg."""

# Afișați pe ecran tipul de date pentru două dintre variabilele definite anterior.

print(type(var_int))  # Afișează tipul pentru var_int
print(type(var_string))  # Afișează tipul pentru var_real

#Pentru una dintre variabilele text definite, afișați lungimea șirului de text.

print(len(var_text_lung))  # Afișează lungimea textului din var_text_lung


#Transformați textul, salvat într-una dintre variabilele text, în litere mari.

print(var_text_scurt.upper())  # Transformă textul în litere mari

# „Tăiați” un subșir dintr-o variabilă text folosind operatorul de acces []

subsir = var_text_lung[0:5]  # Tăiem primele 5 caractere din text
print(subsir)

#Afișați un mesaj pe ecran folosind formatarea șirului textual (prin metoda string.format() și f“string”),
#și incluzând în text valorile atribuite anterior câtorva variabile.

print("Valoarea integer: {}, Valoarea string: {}".format(var_int, var_string))
print(f"Textul scurt: {var_text_scurt}, Textul lung: {var_text_lung}")

age = var_int
t = "Age: {}, Valoarea string: {}"
a = t.format(age, var_string)
print(a)


b= f"Textul scurt: {var_text_scurt}, Textul lung:{var_text_lung}"
print(b)


#Sarcina 2
txt = "More results from text..."
substr = txt[4:12]
print(substr)  # Va afișa "results"
t = substr.strip()
print(t)  # Va afișa "results" fără spații, dar nu are diferență pentru acest caz

a = []
b = a
a.append(9)



#b)
txt = "More results from text..."
o = (txt.split())  # Va împărți textul în liste de cuvinte
print(txt)
o.append(var_string + str(var_int))
print(o)
print(type(o))
o1 = (txt.split())

#c)
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))  # Va înlocui {} cu valoarea age

