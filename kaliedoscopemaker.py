import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Kaliedoscopefilter")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    
    
    
    running = True
    while running:
        # silly events
        screen.fill((0,0,0))
        
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #pygame update
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()