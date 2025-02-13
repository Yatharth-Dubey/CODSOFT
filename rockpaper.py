import pygame
import random

pygame.mixer.init()
pygame.init()

# Game Window Dimensions
screen_width = 500
screen_height = 500

# Colors
black = (0, 0, 0)
orange = (255, 145, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

bg = pygame.image.load("Background.jpg")
bg = pygame.transform.scale(bg, (200, 150))

# Load Background Images
bg_frame = pygame.image.load("border.jpg")
bg_frame = pygame.transform.scale(bg_frame, (550, 550))

bg2 = pygame.image.load("game_background.jpg")
bg2 = pygame.transform.scale(bg2, (screen_width, screen_height))

# Load Rock, Paper, Scissors Images
rock_img = pygame.image.load("rock.jpg")
paper_img = pygame.image.load("paper.jpg")
scissors_img = pygame.image.load("scissors.jpeg")

# Resize Images
rock_img = pygame.transform.scale(rock_img, (80, 80))
paper_img = pygame.transform.scale(paper_img, (80, 80))
scissors_img = pygame.transform.scale(scissors_img, (80, 80))

# Game Window Setup
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("YATHARTH's ROCK PAPER SCISSORS")

# Font
font = pygame.font.SysFont("Comic Sans MS", 40)

# Score Tracking
player_score = 0
computer_score = 0
result_text = ""
score_font_size = 30  # Default size

# Function to render text on screen
def text_screen(text, color, x, y, size=40):
    font = pygame.font.SysFont("Comic Sans MS", size)
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

# Function to create rounded images
def create_round_image(image, size):
    image = pygame.transform.smoothscale(image, size)
    mask = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(mask, (255, 255, 255, 255), (size[0] // 2, size[1] // 2), size[0] // 2)
    round_image = pygame.Surface(size, pygame.SRCALPHA)
    round_image.blit(image, (0, 0))
    round_image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    return round_image

# Create Buttons
buttons = {
    "rock": (100, 350),
    "paper": (210, 350),
    "scissors": (320, 350)
}

rock_button = create_round_image(rock_img, (80, 80))
paper_button = create_round_image(paper_img, (80, 80))
scissors_button = create_round_image(scissors_img, (80, 80))

# Reset Button
def draw_reset_button():
    pygame.draw.rect(gamewindow, white, (165, 450, 120, 40), border_radius=10)
    text_screen("Reset", black, 190, 455, 25)

# Function to determine the game logic
def logic(choice):
    global result_text, player_score, computer_score, score_font_size

    choices = {"rock": 1, "paper": 2, "scissors": 3}
    no_choice = choices[choice]  # Player's choice as a number

    computer_choice = random.randint(1, 3)  # 1 = Rock, 2 = Paper, 3 = Scissors
    com_choice = list(choices.keys())[computer_choice - 1]  # Get the choice name

    # Determine winner
    if com_choice == choice:
        result_text = "It's a Draw! Play Again"
    elif (no_choice == 1 and computer_choice == 3) or \
            (no_choice == 2 and computer_choice == 1) or \
            (no_choice == 3 and computer_choice == 2):
        result_text = "You Win! Play Again"
        player_score += 1
    else:
        result_text = "Computer Wins! Play Again"
        computer_score += 1

# Function to show a splash screen before the game starts
def showscreensplash(image, durationtime=3):
    gamewindow.blit(image, (0, 0))
    pygame.display.update()
    pygame.time.delay(durationtime * 1000)

# Welcome screen
def welcome():
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play(-1)
    showscreensplash(bg2, 2)
    gameloop()

# Main Game Loop
def gameloop():
    global result_text, player_score, computer_score, score_font_size
    exit_game = False
    clock = pygame.time.Clock()

    while not exit_game:
        gamewindow.fill(black)
        gamewindow.blit(bg_frame, (-25, -25))
        gamewindow.blit(bg, (150,150))
        gamewindow.blit(rock_button, buttons["rock"])
        gamewindow.blit(paper_button, buttons["paper"])
        gamewindow.blit(scissors_button, buttons["scissors"])
        draw_reset_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                # Detect button clicks
                for choice, (x, y) in buttons.items():
                    distance = ((mx - (x + 40)) ** 2 + (my - (y + 40)) ** 2) ** 0.5
                    if distance < 40:
                        logic(choice)
                
                # Check if reset button is clicked
                if 180 <= mx <= 320 and 450 <= my <= 490:
                    player_score = 0
                    computer_score = 0
                    result_text = ""
                    score_font_size = 40
        
        # Display Scores & Result
        text_screen(f"Player: {player_score}", green, 30, 20, score_font_size)
        text_screen(f"Computer: {computer_score}", blue, 295, 20, score_font_size)
        text_screen(result_text, orange, 20, 80)
        
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

welcome()
