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

while running:
    screen.fill((0, 0, 0))  # Fill screen with black (background)
    screen.blit(background, (0, 0))  # Draw background image

    for event in pygame.event.get():  # Process all game events
        if event.type == pygame.QUIT:  # If window close button clicked
            running = False  # Exit game loop
        
        if event.type == pygame.KEYDOWN:  # If key is pressed
            if event.key == pygame.K_LEFT:  # Left arrow key
                playerX_change = -5  # Move player left
            if event.key == pygame.K_RIGHT:  # Right arrow key
                playerX_change = 5  # Move player right
            if event.key == pygame.K_SPACE and bullet_state == "ready":  # Space key to fire
                bulletX = playerX  # Set bullet start position to player position
                fire_bullet(bulletX, bulletY)  # Fire bullet
        
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:  # Key released
            playerX_change = 0  # Stop player movement

    # Player Movement
    playerX += playerX_change  # Update player position

# Player Movement
    playerX += playerX_change  # Update player position
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # Keep player within screen bounds (64 is player size)
    

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition (enemy reached bottom)
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move all enemies off-screen
            game_over_text()  # Show game over message
            break  # Exit loop

        enemyX[i] += enemyX_change[i]  # Move enemy horizontally
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:  # If enemy hits screen edge
            enemyX_change[i] *= -1  # Reverse horizontal direction
            enemyY[i] += enemyY_change[i]  # Move enemy down

    # Collision Check
    if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):  # If bullet hits enemy
        bulletY = PLAYER_START_Y  # Reset bullet position
        bullet_state = "ready"  # Reset bullet state


# Player Movement
    playerX += playerX_change  # Update player position
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # Keep player within screen
    # bounds (64 is player size)

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition (enemy reached bottom)
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move all enemies off-screen
            game_over_text()  # Show game over message
            break  # Exit loop

        enemyX[i] += enemyX_change[i]  # Move enemy horizontally
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:  # If enemy hits screen edge
            enemyX_change[i] *= -1  # Reverse horizontal direction
            enemyY[i] += enemyY_change[i]  # Move enemy down

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):  # If bullet hits enemy
            bulletY = PLAYER_START_Y  # Reset bullet position
            bullet_state = "ready"  # Reset bullet state
            score_value += 1  # Increase score
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)  # Respawn enemy at random X
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)  # Respawn enemy at random Y

        enemy(enemyX[i], enemyY[i], i)  # Draw enemy

    # Bullet Movement
    if bulletY <= 0:  # If bullet goes off top of screen
        bulletY = PLAYER_START_Y  # Reset bullet position
        bullet_state = "ready"  # Reset bullet state
    elif bullet_state == "fire":  # If bullet is active
        fire_bullet(bulletX, bulletY)  # Draw bullet
        bulletY -= bulletY_change  # Move bullet upward

    player(playerX, playerY)  # Draw player
    show_score(textX, textY)  # Draw score





# Player Movement
    playerX += playerX_change  # Update player position
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # Keep player within screen
    # bounds (64 is player size)

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition (enemy reached bottom)
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move all enemies off-screen
            game_over_text()  # Show game over message
            break  # Exit loop

        enemyX[i] += enemyX_change[i]  # Move enemy horizontally
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:  # If enemy hits screen edge
            enemyX_change[i] *= -1  # Reverse horizontal direction
            enemyY[i] += enemyY_change[i]  # Move enemy down

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):  # If bullet hits enemy
            bulletY = PLAYER_START_Y  # Reset bullet position
            bullet_state = "ready"  # Reset bullet state
            score_value += 1  # Increase score
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)  # Respawn enemy at random X
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)  # Respawn enemy at random Y

        enemy(enemyX[i], enemyY[i], i)  # Draw enemy

    # Bullet Movement
    if bulletY <= 0:  # If bullet goes off top of screen
        bulletY = PLAYER_START_Y  # Reset bullet position
        bullet_state = "ready"  # Reset bullet state
    elif bullet_state == "fire":  # If bullet is active
        fire_bullet(bulletX, bulletY)  # Draw bullet
        bulletY -= bulletY_change  # Move bullet upward

    player(playerX, playerY)  # Draw player
    show_score(textX, textY)  # Draw score
    pygame.display.update()  # Update the display

