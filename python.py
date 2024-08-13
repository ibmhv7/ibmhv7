import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CAR_COLOR = (255, 0, 0)
FPS = 60

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Racing Game")

# Load car image
# car_image = pygame.image.load('car.png')  # Use an image file if you have one
car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(CAR_COLOR)

# Car properties
car_x = SCREEN_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10
car_speed = 5

# Set up the clock
clock = pygame.time.Clock()

def game_loop():
    global car_x, car_y
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        if keys[pygame.K_RIGHT]:
            car_x += car_speed
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw the car
        screen.blit(car_image, (car_x, car_y))
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
