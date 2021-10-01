import pyglet
from string import ascii_lowercase

window = pyglet.window.Window()

label = pyglet.text.Label("Hello world", x=window.width // 2, y=window.height // 2)


@window.event
def on_draw():
    window.clear()
    label.draw()


@window.event
def on_key_press(symbol: int, modifier: int):
    letter = chr(symbol)
    if letter not in ascii_lowercase:
        return
    label.text = letter


pyglet.app.run()
