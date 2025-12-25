import pygame
import constants
import player
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    clock =pygame.time.Clock()
    dt=0
    cplay=player.player(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2)
    screen=pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        cplay.update(dt)
        cplay.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)
        dt/=1000

if __name__ == "__main__":
    main()
