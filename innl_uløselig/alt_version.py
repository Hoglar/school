from math import e

# Kan jeg kjøre fort til jeg går forbi, så snu og halvere for eksempel
def get_a(x):
    return e**x

def get_b(x):
    return 4*x
# a = e**x
# b = 4*x

def find_x_value(x, changer):
    x = x
    increment = 1
    changer = changer
    snuinger = 0

    while True:
        a = get_a(x)
        b = get_b(x)
        diff = a - b
        if round(a, 15) == round(b, 15):
            print(f"Vi har en løsning: {x} etter {snuinger} snuinger.")
            return x

        x += increment
        if diff*changer < 0:
            #snu
            snuinger += 1
            changer = changer * (-1)
            increment = increment/(-10)
        # Eller så fortsetter vi med stor inc

second_x = find_x_value(0, 1) + 0.01
find_x_value(second_x, -1)