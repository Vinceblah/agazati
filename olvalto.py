print("2. feladat: Régi hosszmérték")

usernums = []

for i in range(1,4):
    user = int(input(f"Adja meg az {i}. ölben mért értéket: "))
    ol = user * 1.896 
    print(f"Az {i}. öl adat átszámolva: {ol} méter")
