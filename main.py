import pygame
import constants
import player
import asteroids
import sys
import asteroid_field
import shot
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen=pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    clock =pygame.time.Clock()
    dt=0
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    astra=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    player.player.containers=(updatable, drawable)
    asteroids.Asteroid.containers=(astra,updatable,drawable)
    asteroid_field.AsteroidField.containers=(updatable)
    shot.Shot.containers=(shots,drawable,updatable)
    player_obj=player.player(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2)
    astrof_obj=asteroid_field.AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt=clock.tick(60)/1000
        updatable.update(dt)
        player_obj.cooldown-=dt
        for castra in astra:
            if player_obj.collides_with(castra):
                print("Game over!")
                sys.exit()
        for castra in astra:
            for gun in shots:
                if castra.collides_with(gun):
                    gun.kill()
                    castra.split()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
