
from helper import sin_deg
#Trekant 1:
# Lage et program som tar vinkel A og vinkel B og lengden AB som input
    # To typer input, sjekke for parametere, eller ta input.

# Vi har tre vinkler i en trekant, hver med sin motstående side.
# Vinkel A har side a, B har b og C har c, a = BC, b = AC og c = AB

# pair består av vinkel, og lengde på motstående side. 


pair_a = [0, None]
pair_b = [0, None]
pair_c = [0, None]


def get_angle(name):

    #Lage en sjekke vinkel funksjon?
    leftover_angle = 180
    if not pair_a[0] and not pair_b[0] and not pair_c[0]:
        print("Dont have any angles yett")
        pass

    elif bool(pair_a[0]) + bool(pair_b[0]) + bool(pair_c[0]) == 1:
        print("Har vinkel A, kan finne en til")
        leftover_angle = leftover_angle - pair_a[0] - pair_b[0] - pair_c[0]
    
    while True:
        try:
            angle = input(f"Hvor stor en vinkel {name}? ")

            if angle =="":
                return 0
            else:
                angle = float(angle)
            
            if 0 < angle < leftover_angle: 
                return angle
            else:
                print(f"Du skal skrive vinkelen til {name}. Mellom 0 og {leftover_angle} grader.")
        except ValueError as e:
            print(f"Du kan ikke skrive bokstaver!\nError:{e}")

print("Hei, du får nå noen sprørsmål angående vinklene og sidene i trekanten: ")


pair_a[0] = get_angle("A")
pair_b[0] = get_angle("B")
pair_c[0] = get_angle("C")

if bool(pair_a[0]) + bool(pair_b[0]) + bool(pair_c[0]) == 2:
    angle = leftover_angle - pair_a[0] - pair_b[0] - pair_c[0]
    print(f"Setting remaining angle to {angle}")

    if not pair_a[0]:
        pair_a[0] = angle
    elif not pair_b[0]:
        pair_b[0] = angle
    else:
        pair_c[0] = angle

print(pair_a[0], pair_b[0], pair_c[0])

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



# Finner arealet

#def find_triangle_side(known_pair, unkown_pair):
