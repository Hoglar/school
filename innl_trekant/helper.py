from math import sin, cos, radians, acos, asin, degrees, sqrt
import sys

def sin_deg(x):
    radian = radians(x)
    return sin(radian)

def cos_deg(x):
    radian = radians(x)
    return cos(radian)

def reverse_cos(x):
    rad_angle = acos(x)
    return degrees(rad_angle)

def reverse_sin(x):
    try:
        rad_angle = asin(x)
    except ValueError:
        sys.exit("Unsolvable")
    return degrees(rad_angle)


    

# Kan lage en del funksjoner som finner sider og vinkler basert på hva jeg har

# Lager en funksjon som sjekker par, får så tilbake "none", "both", "angle", "side"
# Ikke planlagt hvordan den skal brukes, men tror det kan bli bra.

# Tar list som parameter, list inneholder [vinkel, side]
def check_pair(pair: list):
    if not pair[0] and not pair[1]:
        return None
    elif pair[0] and not pair[1]:
        return "angle"
    elif not pair[0] and pair[1]:
        return "side"
    else:
        return "both"
    
# Skal brukes i filter , tar pair, sjekker om jeg har både vinkel og side.
def is_pair_done(pair: list) -> bool:
    if pair[0] and pair[1]:
        return True
    else:
        return False
    
# Lager et scoring system, trur at det kan hjelpe med å avgjøre om det kan løses eller ikke

def triangle_score(pairs: list) -> int:
    merged_pairs = [item for sublist in pairs for item in sublist]
    score = 0
    for x in merged_pairs:
        if x:
            score += 1
    return score

def check_sides(a:int, b:int, c:int) -> bool:
    # a+b>c,a+c>b,b+c>a
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False




# Cosinussetingen for vinkler
# Viktig å putte in par du vil finne i a, de to andre kan gå der de vil. 
def cosset_find_angle(a: list, b: list, c: list) -> int:

    if not a[0]:

        cos_a = (pow(b[1],2) + pow(c[1], 2) - pow(a[1], 2))/(2*b[1]*c[1])

        return round(reverse_cos(cos_a), 1)
    else:
        return a[0]

# Hvis jeg har vinkel, mangler side, og har de to andre sidene
def cosset_find_side(a: list, b: list, c: list):
    if a[0] and not a[1] and b[1] and c[1]:
        side = sqrt(pow(b[1], 2) + pow(c[1], 2) - (2 * b[1] * c[1] * cos_deg(a[0])))
        return round(side, 1)
    else:
        return a[1]
    
def sinset_find_side(a: list, b:list) -> int:
    # a har ukjent side, b er kjent
    
    if not a[1] and a[0]:
        side = (b[1] * sin_deg(a[0]))/sin_deg(b[0])
        print("Brukes denne")
        return side
    else:
        return a[1]
    # Prøve å fikse ambiguens, dette ble velidg rotete


def sinset_find_angle(a: list, b: list):
    
    sin_angle = (sin_deg(b[0]) * a[1])/b[1]
    
    angle = round(reverse_sin(sin_angle), 1)
    return angle

    
            
def check_if_extra_triangle(start_angle, angle):

    alt_angle = 180 - angle

    if start_angle[0] >= 90:
        return 0
    elif alt_angle + start_angle[0] < 180:
        return alt_angle

