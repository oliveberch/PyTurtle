import turtle
import math

pointer = turtle.Turtle()
pointer.speed(700)

window = turtle.Screen()
window.bgcolor("#000000")
pointer.color("yellow")

cord = 20

pointer.left(90)
pointer.penup()
pointer.goto(-7 * cord, 0)
pointer.pendown()

for a in range(-7 * cord, -3 * cord, 1):
    x = a / cord
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    pointer.goto(a, y * cord)

for a in range(-3 * cord, -1 * cord - 1, 1):
    x = a / cord
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    pointer.goto(a, y * cord)

pointer.goto(-1 * cord, 3 * cord)
pointer.goto(int(-0.5 * cord), int(2.2 * cord))
pointer.goto(int(0.5 * cord), int(2.2 * cord))
pointer.goto(1 * cord, 3 * cord)
print("Batman Logo with Python Turtle")
for a in range(1 * cord + 1, 3 * cord + 1, 1):
    x = a / cord
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    pointer.goto(a, y * cord)

for a in range(3 * cord + 1, 7 * cord + 1, 1):
    x = a / cord
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    pointer.goto(a, y * cord)

for a in range(7 * cord, 4 * cord, -1):
    x = a / cord
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    pointer.goto(a, y * cord)

for a in range(4 * cord, -4 * cord, -1):
    x = a / cord
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    pointer.goto(a, y * cord)

for a in range(-4 * cord - 1, -7 * cord - 1, -1):
    x = a / cord
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    pointer.goto(a, y * cord)

pointer.penup()
pointer.goto(300, 300)
turtle.done()