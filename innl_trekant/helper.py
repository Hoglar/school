from math import sin, radians

def sin_deg(x):
    radian = radians(x)
    return sin(radian)

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
    