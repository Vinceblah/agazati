x = int(input("Adj meg egy kordinatat: "))
y = int(input("Adj meg egy kordinatat: "))


def siknegyed(x,y):
    if x and y > 0:
        vissza = "A pont az első síknegyedben van."
    if x < 0 and y > 0:
        vissza =" A pont az második síknegyedben van."    
    if x and y < 0:
        vissza =" A pont az harmadik síknegyedben van."
    if x > 0 and y < 0:
        vissza =" A pont az negyedik síknegyedben van."

    if y == 0 and x != 0:
        vissza =" A pont rajta van az x tengelyen."
    
    if x == 0 and y != 0:
        vissza =" A pont rajta van az y tengelyen."
    
    if x == 0 and y == 0:
        vissza =" A pont az origóban van."
    return vissza

ertek = siknegyed(x,y)

print(ertek)