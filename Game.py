# Import necessary libaries
import pygame # For game development functionality 
import random # For random number generation 

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500,400 # Dimensions of the game window 
MOVEMENT_SPEED = 5 # How fast the sprite moves 
FONT_SIZE = 72 # Size of the font for the win message 

# Initialize Pygame - this must be called before using any Pygame functions
pygame.init()

# Load and transform the beging for efficiency
# First load the image file, then scale it to match our screen dimensions
background_image = pygame.transform.scale(pygame.image.load("image.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load font once at the beginning for efficiency
# Using Times New Roman with our predefined size
font = pygame.font.SysFont("Time New Roman", FONT_SIZE)

# Define a Sprite class that inherits from Pygame's Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        # Call the parent class (pygame.sprite.Sprite) constructor
        super().__init__()

        # Create a blank image surface for the sprite
        self.image = pygame.Surface((width, height))

        # Fill the entire surface with a blue color as background
        self.image.fill(pygame.Color("dodgerblue"))

        # Draw a rectangle with the specified color on top  of the blue background
        pygame.draw.rect(self.image, color, pygame.Rect(0,0, width, height))

        # Get the rectangular area of the image for positioning and collision detection
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        # Update x position with boundary checking:
        # - Ensures sprite doesn't go off the right side of the screen 
        # - Ensures sprite doesn't go off the left side of the screen 
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0 )

    
        # Update y position with boundary checking:
        # - Ensures sprite doesn't go off the bottom side of the screen 
        # - Ensures sprite doesn't go off the top side of the screen 
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0 )

# Game setup section
# Create the display window with our predefined dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(":Sprite Collision") # Set window title

# Create a grounp to hold all sprite form easy drawing and management 
all_sprites = pygame.sprite.Group()

# Creating first sprite (black rectangle)
sprite1 = Sprite(pygame.Color("black"), 30, 30) # 30x30 red rectangle
# Set random intial position within screen bounds
sprite1.rect.x, sprite1.rect.y = random(0, SCREEN_WIDTH - sprite1.rect.width),random.randint(0,SCREEN_HEIGHT - sprite1.rect.height)

all_sprites.add(sprite1) #Add to sprite group
