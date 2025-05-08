import sys
import pygame

class AlienInvasion:
    """Class to manage game assets and behaviour."""
    def __init__(self):
        """Initialise the game and create game resources."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game