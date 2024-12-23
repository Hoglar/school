
from helper import (sin_deg, check_pair, is_pair_done, 
                    triangle_score, cosset_find_angle, check_sides,
                    cosset_find_side, sinset_find_side, sinset_find_angle, check_if_extra_triangle)
from turtle_paint import draw_triangle

#Trekant 1:
# Lage et program som tar vinkel A og vinkel B og lengden AB som input
    # To typer input, sjekke for parametere, eller ta input.

# Vi har tre vinkler i en trekant, hver med sin motstående side.
# Vinkel A har side a, B har b og C har c, a = BC, b = AC og c = AB

# pair består av vinkel, og lengde på motstående side. 

pair_a = [0, 0]
pair_b = [0, 0]
pair_c = [0, 0]
# Sette in triangle her, bytte ut pair
do_we_have_extra = False
alt_a = [0, 0]
alt_b = [0, 0]
alt_c = [0, 0]
alt_triangle = [alt_a, alt_b, alt_c]
done = False

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
pairs = [pair_a, pair_b, pair_c]

alt_a[0], alt_a[1] = pair_a[0], pair_a[1]
alt_b[:2] = pair_b[:2]
alt_c[:2] = pair_c[:2]

#Hvorfor må den kjøre så mange ganger?
for i in range(6):

    # End program om vi har tilfeller som ikke kan løses
    # Må ha mer en 1 side og en vinkel. Går heller ikke med 3 vinkler, 3 sider derimot er greit
    if triangle_score(pairs) < 3:
        print("Har ikke noe informasjon, får ikke løst trekanten")
        break
    elif all(check_pair(pair) in ["angle"] for pair in pairs):
        print("Har bare vinkler, kan ikke løse")
        break

    # Kan nå starte med matte!
    # Hvis jeg bare har sider, finner jeg bare vinklene.
    # Kan her ta litt error handling og tror jeg. Finnes regler her, men må utforske litt
    if all(check_pair(pair) in ["both", "side"] for pair in pairs):
        if check_sides(pair_a[1], pair_b[1], pair_c[1]):

            pair_a[0] = cosset_find_angle(pair_a, pair_b, pair_c)
            pair_b[0] = cosset_find_angle(pair_b, pair_a, pair_c)
            pair_c[0] = cosset_find_angle(pair_c, pair_a, pair_b)
        else:
            print("Ser ikke ut som det kan finnes noen trekant med sidene du ga.")
            break
    
    # hvis pair 1 har vinkel og par 2 og 3 har side, kan vi finne side til 1
    # Bare prøve å bruke den, enten fikser den, eller så gjør den ingenting.
    pair_a[1] = cosset_find_side(pair_a, pair_b, pair_c)
    pair_b[1] = cosset_find_side(pair_b, pair_a, pair_c)
    pair_c[1] = cosset_find_side(pair_c, pair_a, pair_b)

    #Kunne kanskje vært bedre her.

    # Da er det igjen Sinus setningen
    done_pairs = [x for x in pairs if is_pair_done(x)]


    # Har to sinset funksjoner, en som returner vinkel, og en som returner side. 
    # Den som returner vinkel må jeg være obs på. Lager side først
    
    pair_a[1] = sinset_find_side(pair_a, done_pairs[0])
    pair_b[1] = sinset_find_side(pair_b, done_pairs[0])
    pair_c[1] = sinset_find_side(pair_c, done_pairs[0])


    # Må nå sjekke om jeg kan ha flere trekanter.
    # Om 2 trekanter, kanskje jeg kan kjøre ny trekant gjennom samme løkke?
    # den andre trekanten må ha infor jeg har til nå. det er resten som endres
    # Så herfra finner jeg 2 trekanter

    #Dette kan nok løses bedre
    # Par A
    #Om jeg klarer meg uten sin er det bra
    if i > 1:
        if not pair_a[0] and pair_a[1]:
            pair_a[0] = sinset_find_angle(pair_a, done_pairs[0])
            alt = check_if_extra_triangle(done_pairs[0], pair_a[0])
            if alt:
                alt_a[0] = alt
                alt_a[1] = pair_a[1]
                do_we_have_extra = True
            
        elif not pair_a[0] and not pair_a[1] and bool(pairs[0][0]) + bool(pairs[1][0]) + bool(pairs[2][0]) == 2:
            pair_a[0] = round(180 - pairs[0][0] - pairs[1][0] - pairs[2][0], 1)
        # Par B
        if not pair_b[0] and pair_b[1]:
            pair_b[0]  = sinset_find_angle(pair_b, done_pairs[0])
            alt = check_if_extra_triangle(done_pairs[0], pair_b[0])
            if alt:
                alt_b[0] = alt
                alt_b[1] = pair_a[1]
                do_we_have_extra = True
            
        elif not pair_b[0] and not pair_b[1] and bool(pairs[0][0]) + bool(pairs[1][0]) + bool(pairs[2][0]) == 2:
            pair_b[0] = round(180 - pairs[0][0] - pairs[1][0] - pairs[2][0], 1)
        #Par C
        if not pair_c[0] and pair_c[1]:
            pair_c[0]  = sinset_find_angle(pair_c, done_pairs[0])
            alt = check_if_extra_triangle(done_pairs[0], pair_c[0])
            if alt:
                alt_c[0] = alt
                alt_c[1] = pair_a[1]
                do_we_have_extra = True
            
        elif not pair_c[0] and not pair_c[1] and bool(pairs[0][0]) + bool(pairs[1][0]) + bool(pairs[2][0]) == 2:
            pair_c[0] = round(180 - pairs[0][0] - pairs[1][0] - pairs[2][0], 1)


        done_pairs = [x for x in pairs if is_pair_done(x)]

    if len(done_pairs) == 3:
        done = True
        break

if do_we_have_extra:
    done_pairs = [x for x in pairs if is_pair_done(x)]
    # Vil her altid ha 2 vinkler

    rem_angle = 180 - alt_a[0] - alt_b[0] - alt_c[0]

    if not alt_a[0]:
        alt_a[0] = rem_angle
    elif not alt_b[0]:
        alt_b[0] = rem_angle
    else:
        alt_c[0] = rem_angle

    alt_a[1] = sinset_find_side(alt_a, done_pairs[0])
    alt_b[1] = sinset_find_side(alt_b, done_pairs[0])
    alt_c[1] = sinset_find_side(alt_c, done_pairs[0])

# We can do areal in the end. 
#Hvis jeg ikke finner trekanten , finner jeg ikke arealet.
if done:
    #0.5 * AB * AC * sin A
    areal = round(0.5 * pair_c[1] * pair_b[1] * sin_deg(pair_a[0]), 1)
    print(
        f"\n\nVi har trekant medvinklene:\nA: {pair_a[0]}\nB: {pair_b[0]}\nC: {pair_c[0]}\n\n"
        f"Sidene\nAB: {pair_c[1]}\nBC: {pair_a[1]}\nAC: {pair_b[1]}\n\n"
        f"Med arealet: {areal}"
     )
    
    if do_we_have_extra:
        print(f"Vi har og en ekstra trekant: {alt_triangle}")

    visual = input("Hvis du vil se visuelt eksempel skriv y: ")
    if visual == "y":
        draw_triangle(pair_a, pair_b, pair_c)
    

    




    



    
