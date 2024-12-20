
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
    else:
        return 0
    
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

# Tar her imot pair som argumenter, så den blir mere modulær.
def get_side(side_name, a, b, c):
    print(a, b , c)
    # Starter med å innhente data fra bruker. Sidene må være positive, men ingen maks grense.
    # om jeg har 2 sider, vil den tredje kunne bli regnet ut. Kan jobbe lit med å
    # Ta mindre input fra bruker, da jeg kan finne alt om jeg har alle vinkler
    # Kan ta samme aproach, om jeg har 2 sider, så regner jeg ut den siste. 
    # Må kanskje her ta hensyn til 2 løsninger for noen trekanter. 
    while True:
        
        # ingen sider, da henter vi inn fra bruker og setter side. Kan sjekke at den er positiv
        try:
            side_value = input(f"Hva er lengden på {side_name}? ")
            if side_value == "":
                return 0
            else:
                side_value = float(side_value)
            
            if side_value > 0:
                return side_value
            else:
                print("Noe gikk galt, skriv tall større en 0 eller enter om du ikke har tall.")

        except ValueError as e:
            print(f"Noe gikk galt prøvde du å skrive tall med bokstaver?\nError: {e}")

print("Hei, du får nå noen sprørsmål angående vinklene og sidene i trekanten: ")


pair_a[0] = get_angle("A")
pair_b[0] = get_angle("B")
pair_c[0] = get_angle("C")

# Finner siste vinkel om vi har 2 vinkler etter input.

if bool(pair_a[0]) + bool(pair_b[0]) + bool(pair_c[0]) == 2:
    angle = 180 - pair_a[0] - pair_b[0] - pair_c[0]
    print(f"Setting remaining angle to {angle}")

    if not pair_a[0]:
        pair_a[0] = angle
    elif not pair_b[0]:
        pair_b[0] = angle
    else:
        pair_c[0] = angle

# Da kan vi hente inn sider.
pair_c[1] = get_side("AB", pair_a, pair_b, pair_c)
pair_a[1] = get_side("BC", pair_a, pair_b, pair_c)
pair_b[1] = get_side("AC", pair_a, pair_b, pair_c)

#Nå kan vi kanskje få sider som ikke er gyldige, Kan feilsøke det litt, men trur jeg venter.

print(pair_a, pair_b, pair_c)