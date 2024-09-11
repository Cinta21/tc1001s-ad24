from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle_shape(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # Calcula el radio como la mitad de la distancia entre start y end en el eje x
    radius = abs(end.x - start.x) / 2
    goto(start.x + radius, start.y)  # Mover a la posición inicial del círculo
    circle(radius)  # Dibuja el círculo
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.y - start.y))
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Funciones para cambiar de color
onkey(lambda: color('black'), 'K')  # Color negro
onkey(lambda: color('white'), 'W')  # Color blanco
onkey(lambda: color('green'), 'G')  # Color verde
onkey(lambda: color('blue'), 'B')   # Color azul
onkey(lambda: color('red'), 'R')    # Color rojo
onkey(lambda: color('yellow'), 'Y')  # Color amarillo

# Funciones para seleccionar la figura
onkey(lambda: store('shape', line), 'l')        # Dibujar línea
onkey(lambda: store('shape', square), 's')      # Dibujar cuadrado
onkey(lambda: store('shape', circle_shape), 'c')      # Dibujar círculo (usando circle_shape)
onkey(lambda: store('shape', rectangle), 'r')   # Dibujar rectángulo
onkey(lambda: store('shape', triangle), 't')    # Dibujar triángulo

# Función para deshacer la última acción
onkey(undo, 'u')

done()
