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
    except ValueError:
        print("Du må skrive inn et tall!")

while True:
    try: 
        vinkel_b = float(input("Hvor stor er vinkel B? "))

        if 

    except ValueError:
        print("Du må skrive tall!")

print(vinkel_a)

# Sjekker om input er konsistent


# Regner ut de ukjente vinklene 


# og sidene


# Finner arealet
