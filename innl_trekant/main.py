
from helper import sin_deg
#Trekant 1:
# Lage et program som tar vinkel A og vinkel B og lengden AB som input
    # To typer input, sjekke for parametere, eller ta input.

print("Hei, du får nå noen sprørsmål angående vinklene og sidene i trekanten: ")

# Vi har tre vinkler i en trekant, hver med sin motstående side.
# Vinkel A har side a, B har b og C har c, a = BC, b = AC og c = AB

# pair består av vinkel, og lengde på motstående side. 
pair_a = [None, None]
pair_b = [None, None]
pait_c = []

#### Fortsett her!
def get_angle(name):
    leftover_angle = 180
    if pair_a[0]:
        leftover_angle = leftover_angle - pair_a[0]
    elif not pair_a[0] and pair_b[0]:
        leftover_angle = leftover_angle - pair_b[0]
    
    while True:
        try:
            angle = input(f"Hvor stor en vinkel {name}? ")

            if angle =="":
                return None
            else:
                angle = float(angle)
            
            if 0 < angle < leftover_angle: 
                return angle
            else:
                print(f"Du skal skrive vinkelen til {name}. Mellom 0 og {leftover_angle} grader.")
        except ValueError as e:
            print(f"Du kan ikke skrive bokstaver!\nError:{e}")


pair_a[0] = get_angle("A")
pair_b[0] = get_angle("B")

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


# Lage en funksjon som finner side bassert på


side_bc = (side_ab * sin_deg(vinkel_a))/sin_deg(vinkel_c)
side_ac = (side_ab * sin_deg(vinkel_b))/sin_deg(vinkel_c)
print(f"Siden AC vil være {round(side_ac, 2)} og side BC vil være {round(side_bc, 2)}")



# Finner arealet

areal = 0.5 * sin_deg(vinkel_a) * side_ab * side_ac

print(f"Arealet er {round(areal, 2)}")


triangle_pair_a = (vinkel_a, side_bc)

#def find_triangle_side(known_pair, unkown_pair):
