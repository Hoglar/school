# Hva er nå dette for en oppgave da.

# ex = 4x
# ex har en graf og 4x har en graf, de vil møtes. spørsmålet er hvor. 
# Tegner i geogebra for å se hvordan de ser ut. 
# Det finnes 2 verdier for x som gir samme tall, altså når e**x = 4x
# 
# jeg kan starte høyt med en og lavt med den andre.
# iterere og sammenligne.
# om forskjellen er stor øker jeg endring, om forskjellen er liten, synker jeg endring. 
# 
# kan igrunn starte på 0. 

from math import e
answers = 0
increment = 1
while answers == 0:
    x = 0
    while x < 4:
        eulerx = e**x
        four_x = 4*x

        if round(eulerx, 7) == round(four_x, 7):
            print(f"Vi har en verdi for x: {x}")
            answers = 1
            second_x = x + 0.01
            break
        
        x += increment

    increment = increment/10

increment = 1

while answers == 1:
    x = second_x
    while x < 4:
        eulerx = e**x
        four_x = 4*x

        if round(eulerx, 5) == round(four_x, 5):
            print(f"Vi har en verdi til for x: {x}")
            answers = 2
            break
        
        x += increment

    increment = increment/10


    

