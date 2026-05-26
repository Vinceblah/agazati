adatok = []
idok = []
nev = []
evszam = []

with open("maraton.txt","r",encoding="UTF-8") as f:
    for sor in f:
        sor = sor.strip()
        if sor:
            reszek = sor.split(",")
            adatok.append(reszek)



    for sor in adatok:
        idok.append(sor[2])
        nev.append(sor[1])
        evszam.append(sor[0])

gyors=min(idok)

ora = int(gyors) // 3600
perc = (int(gyors) % 3600) // 60
masodperc = int(gyors) % 60

print("A legeredményesebb versenyző a maraton futásban 1952 és 1988 közt:")

print(f"Név: {nev[idok.index(gyors)]}")
print(f"Év: {evszam[idok.index(gyors)]}")
print(f"Időeremény: {ora:02d}:{perc:02d}:{masodperc:02d}")
