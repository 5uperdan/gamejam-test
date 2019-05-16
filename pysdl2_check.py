import sys
import sdl2
import sdl2.ext

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("pysdl2 check", size=(800, 600))
    window.show()
    RESOURCES = sdl2.ext.Resources(__file__, "resources")

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(RESOURCES.get_path("Daruma.png"))
    sprite_x = 0
    sprite_y = 0

    spriterenderer = factory.create_sprite_render_system(window)
    
    running = True
    while running and sprite_x < 100 and sprite_y < 100:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        
        sprite_x += 1
        sprite_y += 1
        sprite.position = (sprite_x, sprite_y)

        sdl2.ext.fill(spriterenderer.surface, sdl2.ext.Color(0, 0, 0))

        spriterenderer.render(sprite)

        window.refresh()
        sdl2.SDL_Delay(30)
    return 0

if __name__ == "__main__":
    sys.exit(run())