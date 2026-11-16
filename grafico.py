import turtle
import random

screen = turtle.Screen()
screen.title("Céu noturno")
screen.setup(800, 600)
screen.bgcolor("#080a1e")
screen.tracer(0)

# Mantém a janela do Turtle acima das outras janelas e com foco.
try:
    screen.cv._rootwindow.attributes("-topmost", True)
    screen.cv._rootwindow.focus_force()
except Exception:
    pass

NAVY = "#000080"
PLUM = "#8B008B"

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def lerp(color1, color2, t):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)

    r = round(r1 + (r2 - r1) * t)
    g = round(g1 + (g2 - g1) * t)
    b = round(b1 + (b2 - b1) * t)

    return rgb_to_hex((r, g, b))


def sky():
    for y in range(0, 600, 5):
        pen.color(lerp(NAVY, PLUM, y / 600))
        pen.goto(400, y)
        pen.setheading(0)
        pen.pensize(6)
        pen.pendown()
        pen.forward(800)
        pen.penup()
    screen.update()


def stars():
    for _ in range(80):
        x = random.randint(-400, 400)
        y = random.randint(50, 280)
        size = random.randint(1, 4)
        pen.goto(x, y)
        pen.dot(size, "white")
    screen.update()


def moon():
    pen.goto(-250, 210)
    pen.dot(52, "#AFAFBB")
   # pen.goto(-236, 220)
   # pen.dot(48, NAVY)
    screen.update()


sky()
stars()
moon()

turtle.done()

