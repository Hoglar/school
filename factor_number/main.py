# Lage et program som tar tall, så faktoriserer ned for så å gi tilbake primtallene 
# i stigende rekkefølge.

numbers = []
# tar et tall og returner 2 tall
def get_lowest_prime_num(number: int):
    candidate = 2
    while candidate <= number:
        if number % candidate == 0:
            return candidate
        candidate += 1        
    

# Veldig enkelt trenger vi å ta inn et tall. 
number = int(input("What number do you want to factorize? "))

# Vi deler tall på 2, og ser om det går. Må kanskje bruke noe remainder her?
while True:
    if number > get_lowest_prime_num(number):
        prime = get_lowest_prime_num(number)
        numbers.append(prime)
        number = number / prime
    else:
        numbers.append(int(number))
        break


print(numbers)