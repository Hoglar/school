import turtle


def get_factor(x):
    x = x
    factor = 0
    while True:
        if x > 500:
            x = x / 2
            factor -= 1
        elif x < 100:
            x = x * 2
            factor += 1
        else:
            return factor
        

def draw_triangle(a: list, b: list, c:list):
    factor = get_factor(a[1])
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Trekant")
    skk = turtle.Turtle()
    skk.shape("turtle")

    
    skk.forward(c[1]*(2**factor))
    skk.left(180-b[0])
    skk.forward(a[1]*(2**factor))
    skk.left(180-c[0])
    skk.forward(b[1]*(2**factor))

    turtle.done()