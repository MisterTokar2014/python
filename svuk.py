#pip install pyglet
import pyglet

mus = pyglet.resource.media(name = "soud.mp3")
mus.play
pyglet.app.run()
