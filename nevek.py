print("1. feladat: Nevek hossza")
vezetek = input("Adja meg a vezetéknevét!: ")
kereszt = input("Írja be a keresztnevét is!: ")

if len(kereszt) < len(vezetek):
    print("Az ön vezetékneve hosszabb a keresztnevénél.")

elif len(kereszt) > len(vezetek):
    print("Az ön keresztneve hosszabb a vezetéknevénél.")

else:
    print("Az ön vezeték- és keresztneve egyforma hosszú.")