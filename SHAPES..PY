import pygame

pygame.init()

screen = pygame.display.set_mode((500,400))

WHITE = (255,255,255)
BLUE = (0,0,255)

screen.fill(WHITE)

pygame.draw.rect(screen,BLUE,(200,150,100,50))

pygame.display.flip()
pygame.time.wait(500)
pygame.quit()