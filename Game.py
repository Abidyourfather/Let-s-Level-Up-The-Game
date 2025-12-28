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
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width),random.randint(0,SCREEN_HEIGHT - sprite1.rect.height)


# Creating first sprite (black rectangle)
sprite2 = Sprite(pygame.Color("red"), 20, 20) # 20x20 red rectangle
# Set random intial position within screen bounds
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width),random.randint(0,SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)  # Add to sprite group






all_sprites.add(sprite1) #Add to sprite group
# Game Loop Control Variables
running = True # Controls whether the game is running
won = False # Tracks whether the player has won
clock = pygame.time.Clock() # Add to sprite group


# Main game loop

while running:
    # Event handling - check for user input
    for event in pygame.event.get():
        # Check for window close or 'x' key press to quit
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False # EXIT THE GAME LOOP 

    # Game logic - only process if player hasn't won yet 
    if not won:
        # Get keyboard state for continuous movement 
        keys = pygame.key.get_pressed()

        # Calculate movement in X direction:
        # Right arrow adds MOVEMENT SPEED, Left arrow subtracts MOVEMENT SPEED
        x_change = (keys[pygame.K_RIGHT] - keys [pygame.K_LEFT]) * MOVEMENT_SPEED

        # Calculate movement in y direction:
        # Down arrow adds MOVEMENT SPEED, up arrow subtracts MOVEMENT SPEED
        y_change = (keys[pygame.K_DOWN] - keys [pygame.K_UP]) * MOVEMENT_SPEED

        # Move the player-controlled sprite (sprite1)
        sprite1.move(x_change, y_change)

        # CHECK FOR COLLOSION BETWEEN SP1 AND SP2
        if sprite1.rect.collidedict(sprite2.rect):
            all_sprites.remove(sprite2) # Remove the red sprite
            won = True # Set win state to True

    # Update the display - this makes all our draws visible
    pygame.display.flip()
    # Cap the frame rate at 90 frames per second
    clock. tick(90)

    # Clean up Pygame when the game loop ends
    pygame.quit()