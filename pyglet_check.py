import pyglet

def game_tick(*args, **kwargs):
    daruma = args[1]
    if daruma.x < 100:
        daruma.x += 1
        daruma.y -= 1
        return

window = pyglet.window.Window(800, 600)

@window.event
def on_draw():
    window.clear()
    daruma.draw()

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()
daruma_image = pyglet.resource.image("Daruma.png")
daruma = pyglet.sprite.Sprite(img=daruma_image, x=0, y=552)

#clock = pyglet.clock.Clock()
pyglet.clock.set_fps_limit(30)
pyglet.clock.schedule(game_tick, daruma)

if __name__ == '__main__':

    pyglet.app.run()