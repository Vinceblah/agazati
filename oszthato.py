szam1 = int(input("Adj meg egy szamot: "))
szam2 = int(input("Adj meg egy szamot: "))

harmas = []

for i in range(szam1,szam2):
    if i%3 == 0:
        harmas.append(i)

print(*harmas,sep=",",end=",")