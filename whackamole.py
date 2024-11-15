import pygame, random

def draw_lines(screen):
    for i in range(20):
        pygame.draw.line(screen, (0,0,0), (32*i, 0), (32*i, 511))
    for j in range(16):
        pygame.draw.line(screen, (0,0,0), (0, 32*j), (639, 32*j))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        draw_lines(screen)
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        pygame.display.flip()
        x0, y0 = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0]//32, pos[1]//32
                    if x == x0 and y == y0:
                        screen.fill("light green")
                        draw_lines(screen)
                        x0 = random.randrange(20)
                        y0 = random.randrange(16)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x0*32, y0*32)))
                        pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
