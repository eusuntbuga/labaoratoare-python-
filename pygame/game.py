import pygame       # Biblioteca principala pentru jocuri 2D
import random       # Pentru generarea aleatoare a pozitiei mancarii, bonusurilor, obstacolelor
import sys          # Pentru a putea inchide jocul cu sys.exit()

# Initializare Pygame
pygame.init()

# Dimensiunea ferestrei jocului
WIDTH, HEIGHT = 600, 600

# Marimea unui bloc (folosit pentru sarpe, mancare, obstacole)
BLOCK_SIZE = 20

# Creare fereastra
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")  # Titlul ferestrei

# Definirea culorilor RGB
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 150, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Controlul vitezei jocului
clock = pygame.time.Clock()

# Fontul folosit pentru text
font = pygame.font.SysFont("arial", 30)

# Functie pentru desenarea sarpelui
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Functie pentru desenarea mancarii
def draw_food(food_pos):
    pygame.draw.rect(win, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

# Functie pentru desenarea bonusului (galben)
def draw_bonus(bonus_pos):
    pygame.draw.rect(win, YELLOW, [bonus_pos[0], bonus_pos[1], BLOCK_SIZE, BLOCK_SIZE])

# Functie pentru desenarea obstacolelor
def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(win, BLUE, [obs[0], obs[1], BLOCK_SIZE, BLOCK_SIZE])

# Functie pentru afisarea unui mesaj pe ecran
def message(msg, color, y_offset=0):
    text = font.render(msg, True, color)
    win.blit(text, [WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + y_offset])

# Meniul principal al jocului
def main_menu():
    while True:
        win.fill(BLACK)
        message("🐍 Snake Game", WHITE, -100)
        message("Apasa S pentru Start", WHITE, -30)
        message("Apasa Q pentru Iesire", WHITE, 10)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:      # Apasa S pentru start
                    game_loop()
                elif event.key == pygame.K_q:    # Apasa Q pentru iesire
                    pygame.quit()
                    sys.exit()

# Functia principala a jocului (logica sarpelui)
def game_loop():
    # Pozitia de start a sarpelui
    x = WIDTH // 2
    y = HEIGHT // 2

    # Miscarea initiala (stationar)
    x_change = 0
    y_change = 0

    # Lista care va contine pozitiile sarpelui
    snake = []
    snake_length = 1

    # Generare pozitie aleatoare pentru mancare
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Initializare bonus (nu este activ)
    bonus_x = bonus_y = None
    bonus_timer = 0

    # Lista obstacolelor
    obstacles = []

    # Variabile pentru stare joc
    game_over = False
    game_close = False

    # Bucle principale
    while not game_over:
        while game_close:
            win.fill(BLACK)
            message("Ai pierdut! Apasa R pentru restart sau Q pentru iesire", WHITE, -30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:  # Restart joc
                        game_loop()

        # Verificare taste apasate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Miscare doar intr-o directie, nu poate inversa direct
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = BLOCK_SIZE

        # Actualizeaza pozitia sarpelui
        x += x_change
        y += y_change

        # Verificare coliziune cu peretii
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Redesenare ecran
        win.fill(BLACK)
        draw_food((food_x, food_y))     # Deseneaza mancarea

        if bonus_x is not None:
            draw_bonus((bonus_x, bonus_y))  # Deseneaza bonusul daca exista

        draw_obstacles(obstacles)       # Deseneaza obstacolele

        # Adaugare capul sarpelui la lista
        snake_head = [x, y]
        snake.append(snake_head)

        # Pastreaza doar ultimele n pozitii (lungimea sarpelui)
        if len(snake) > snake_length:
            del snake[0]

        # Coliziune cu propriul corp
        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        # Coliziune cu obstacole
        for obs in obstacles:
            if snake_head == obs:
                game_close = True

        # Deseneaza sarpele
        draw_snake(snake)

        # Afiseaza scorul
        score_text = font.render(f"Scor: {snake_length - 1}", True, WHITE)
        win.blit(score_text, [10, 10])

        # Actualizeaza ecranul
        pygame.display.update()

        # Daca mananca mancarea
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

            # La fiecare 5 puncte adauga un obstacol
            if snake_length % 5 == 0:
                obs_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                obs_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                obstacles.append([obs_x, obs_y])

        # Contor pentru bonus (apare la fiecare 300 de cadre)
        bonus_timer += 1
        if bonus_timer > 300:
            bonus_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            bonus_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            bonus_timer = 0

        # Daca mananca bonusul
        if bonus_x == x and bonus_y == y:
            snake_length += 3     # Bonus: creste cu 3
            bonus_x = bonus_y = None

        # Controlul vitezei jocului (devine mai rapid pe masura ce creste)
        clock.tick(10 + snake_length // 5)

    # Daca jocul se termina
    pygame.quit()
    sys.exit()

# Porneste jocul din meniul principal
main_menu()
