class Helyszin:
    def __init__(self, nev, telepules, evszam):
        self.nev = nev
        self.telepules = telepules
        self.evszam = evszam


print("3. feladat: Helyszínek")

lista = []

for i in range(3):
    nev = input("Adja meg egy helyszín nevét!: ")
    telepules = input("Adja meg a helyszín települését!: ")
    evszam = int(input("Adja meg a létrehozás évszámát!: "))

    hely = Helyszin(nev,telepules,evszam)
    lista.append(hely)

legkorabbi_helyszin = lista[0]

for hely in lista:
    if hely.evszam < legkorabbi_helyszin.evszam:
        legkorabbi_helyszin = hely


with open("legkorabbi.txt", "w", encoding="UTF-8") as f:
    f.write(f"A(z) {legkorabbi_helyszin.nev} a legkorábbi.")

print(f"A legkorábbi évszám: {legkorabbi_helyszin.evszam}")
print("A legkorábban létrehozott hely nevének fájlba írása kész.")