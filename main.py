import pygame
from game import Game
pygame.init()


#Generer la fenetre de notre jeu
pygame.display.set_caption('Comet Fall Game')
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load('assets/bg.jpg')

# Charger un player
# player = Player()
game = Game()

running = True

# boucle

while running:
    #appliquer le background de notre plan de jeu
    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectiles:
        projectile.move()

    for monster in game.all_monsters:
        monster.forward()
    ## appliquer l'ensemble des images du groupes de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images du groupes de monstres
    game.all_monsters.draw(screen)

    # screen.blit(game.player.image, game.player.rect)
    # print(game.pressed)
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -10:
        game.player.move_left()

    #Mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            # Fermeture du jeu
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # print(event.key)
            # detecter si la touche est égale à espace
            # if event.key == pygame.K_ESCAPE:
            if event.key == 32:
                print('espace')
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            # if event.key == pygame.K_RIGHT:
            #     game.player.move_right()
            # elif event.key == pygame.K_LEFT:
            #     game.player.move_left()