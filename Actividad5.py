from random import *
from turtle import *
from freegames import path

car = path('car.gif')
emojis = [
    '😀', '🐍', '🚗', '🚀', '🌟', '🏖', '🎈', '🎁', 
    '🏠', '🍔', '🎲', '⚽️', '📱', '✈️', '📚', '💡',
    '🍕', '🎸', '🐳', '🚴', '🎨', '🧩', '🏆', '🕹️', 
    '🎤', '🍩', '📷', '🎧', '🚤', '🎮', '🌈', '💻', '🏅'
] * 2

shuffle(emojis) 
state = {'mark': None, 'clicks': 0}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    state['clicks'] += 1

    if mark is None or mark == spot or emojis[mark] != emojis[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 5, y)
        color('black')
        write(emojis[mark], align='center', font=('Arial', 30, 'normal'))
    up()

    goto(-190, 195)
    color('black')
    write(f'Clics: {state["clicks"]}', font=('Arial', 18, 'normal'))

    if all(not hidden for hidden in hide):
        goto(0, 0)
        color('green')
        write("¡Juego completado!", align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()