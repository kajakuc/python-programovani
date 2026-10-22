<<<<<<< HEAD
<<<<<<< HEAD
jmeno = input("Jak se jmenuješ?: ")
vek = int(input("Kolik ti je let?: "))

print(f"Ahoj {jmeno}! Za 10 let ti bude {vek + 10} let.")
########
=======
x = None
if "a" in "abracadabra":
    x = True
print(x)
>>>>>>> a5bfd0a (feat)
=======
"""
jmena = ["Josef", "Martin", "Petr", "Marek", "Tadeas", "Jiri"]

# Cvičení 1: Váš kód sem 👇
for i in jmena:
    if "e" in i:
        print(i)
"""


"""
# Cvičení 2: Váš kód sem 👇
for i in range(0,99):
    if i % 2 != 0:
        print(i)
"""



muj_list = [
    "Ostrava",
    "Kladno",
    "Praha",
    "Liberec",
    "Opava",
    "České Budějovice",
    "Litoměřice"
]

vstup = int(input("Zadejte index města: "))

# Cvičení 3: Váš kód sem 👇

for index,i in enumerate(muj_list):
    if vstup > index or vstup < 0:
        print("Chybný vstup")
        break
    elif vstup == index:
        print(f"{index}. město: {i} ← Vybráno")
    else:
        print(f"{index}. město: {i}")
>>>>>>> 4693392 (update)
