
from helper import sin_deg, check_pair, is_pair_done, triangle_score
#Trekant 1:
# Lage et program som tar vinkel A og vinkel B og lengden AB som input
    # To typer input, sjekke for parametere, eller ta input.

# Vi har tre vinkler i en trekant, hver med sin motstående side.
# Vinkel A har side a, B har b og C har c, a = BC, b = AC og c = AB

# pair består av vinkel, og lengde på motstående side. 

pair_a = [0, 0]
pair_b = [0, 0]
pair_c = [0, 0]

def get_angle(name):

    #Lage en sjekke vinkel funksjon?
    leftover_angle = 180
    if not pair_a[0] and not pair_b[0] and not pair_c[0]:
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

# Hvilke muligheter har jeg? vi dropper cos, sin og tan da vi ikke vet om trekanten er rett. 
# Vi tar ikke høyde for at vi muligens har areal, så vi dropper og Arealsetingen.
# Pytagoras utgår da det ikke er retvinklet.
# Vi sitter igjen med sinussetningen og cosinus setningen. 

#Sinus setningen
# Vi trenger 2 vinkler og en side. eller en side og 2 vinkler.
# Om vi har 2 sider og en vinkel er det skumelt, da vi kan få 2 trekanter. 
# Tror det derfor er lurt å løse den til slutt.
# Sin er bra, da jeg ikke trenger orden på hvem par som er hvem, alt er par mot par. 

# Cosinus setningen
# Er fin og ha om jeg har alle sidene.
# Om det er tilfellet kan jeg egentlig bare finne alle vinklene med en gang. 
# Data bryr seg ikke om at cosset er lang
# Cosinus er og tryggere, er den ikke ?

# Så hvor starter vi, først om vi kan løse i det hele tatt. om jeg ikke 

# Må utelukke noen kasuser som ikke kan løses

#Må jeg ha et par? Kan hvertfall finne par, i pairs vil indexen altid vite hvem side og vinkel
pairs =[pair_a, pair_b, pair_c]

while True:

    done_pairs = [x for x in pairs if is_pair_done(x)]
    pairs_to_fix = [x for x in pairs if not is_pair_done(x)]
    print(pairs_to_fix)

    if len(done_pairs) == 3:
        print("Vi er ferdige", done_pairs)
        break

    # End program om vi har tilfeller som ikke kan løses
    # Må ha mer en 1 side og en vinkel. Går heller ikke med 3 vinkler, 3 sider derimot er greit
    if triangle_score(pairs) < 3:
        print("Har ikke noe informasjon, får ikke løst trekanten")
        break
    elif check_pair(pair_a) and check_pair(pair_b) and check_pair(pair_c) == "angle":
        print("Har bare vinkler, kan ikke løse")
        break

    # Kan nå starte med matte!
    

