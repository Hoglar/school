from math import sin
from helper import sin_deg
#Trekant 1:
# Lage et program som tar vinkel A og vinkel B og lengden AB som input
    # To typer input, sjekke for parametere, eller ta input.

print("Hei, du får nå noen sprørsmål angående vinklene og sidene i trekanten: ")

while True:
    try:
        vinkel_a = float(input("Hvor stor er vinkel A? "))

        if 0 < vinkel_a < 180: 
            break
        else:
            print("Du skal skrive vinkelen. Den må være mellom 0 og 180 grader, prøv igjen:")
    except ValueError as e:
        print(f"Du må skrive inn et tall! \nError: {e}")

while True:
    try: 
        vinkel_b = float(input("Hvor stor er vinkel B? "))

        if 0 < vinkel_b < 180 and vinkel_a + vinkel_b < 180:
            break
        else:
            print("Vinkel mellom, 0 og 180, mulig vinklene er for store")

    except ValueError as e:
        print(f"Du må skrive tall! \nError: {e}")


vinkel_c = 180 - vinkel_a - vinkel_b
print(f"Vinkel C vil være: {vinkel_c}")

# Sjekker om input er konsistent


# Regner ut de ukjente vinklene 
while True:
    try:
        side_ab = float(input("Trenger nå lengden på side AB i trekanten: "))

        if side_ab > 0:
            break
        else:
            print("Ikke bruk negative tall!")

    except ValueError as e:
        print(f"brukte du tall?\nError: {e}")

# og sidene

side_bc = (side_ab * sin_deg(vinkel_a))/sin_deg(vinkel_c)
side_ac = (side_ab * sin_deg(vinkel_b))/sin_deg(vinkel_c)
print(f"Siden AC vil være {round(side_ac, 2)} og side BC vil være {round(side_bc, 2)}")



# Finner arealet

areal = 0.5 * sin_deg(vinkel_a) * side_ab * side_ac

print(f"Arealet er {round(areal, 2)}")
