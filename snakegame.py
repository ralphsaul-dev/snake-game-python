import pygame
import random

# Configurações iniciais
largura = 600
altura = 400
snake_size = 10
snake_speed = 15

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)

pygame.init()
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

# Função para mostrar mensagens na tela
def message_display(msg, x, y):
    text = font.render(msg, True, RED)
    screen.blit(text, [x, y])

# Função para desenhar a cobra
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, WHITE, (x, y, snake_size, snake_size))

def game_loop():
    game_over = False
    game_close = False

    snake_x = largura / 2
    snake_y = altura / 2
    x_change = 0
    y_change = 0

    snake_body = []
    snake_length = 1

    food_x = random.randint(0, (largura - snake_size) // 10) * 10
    food_y = random.randint(0, (altura - snake_size) // 10) * 10

    score = 0
    direction = ""

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message_display(f"Game Over! Score: {score}. Press R to Restart or Q to Quit", largura / 6, altura / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x_change = -snake_size
                    y_change = 0
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    x_change = snake_size
                    y_change = 0
                    direction = "RIGHT"
                if event.key == pygame.K_UP and direction != "DOWN":
                    y_change = -snake_size
                    x_change = 0
                    direction = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    y_change = snake_size
                    x_change = 0
                    direction = "DOWN"

        snake_x += x_change
        snake_y += y_change

        # Se a cobra bater na borda, o jogo termina
        if snake_x < 0 or snake_x >= largura or snake_y < 0 or snake_y >= altura:
            game_close = True

        screen.fill(BLACK)

        # Desenha a comida
        pygame.draw.rect(screen, WHITE, (food_x, food_y, snake_size, snake_size))

        # Atualiza o corpo da cobra
        snake_body.append((snake_x, snake_y))
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Se a cobra bater nela mesma, o jogo acaba
        if (snake_x, snake_y) in snake_body[:-1]:
            game_close = True

        draw_snake(snake_body)
        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
            food_x = random.randint(0, (largura - snake_size) // 10) * 10
            food_y = random.randint(0, (altura - snake_size) // 10) * 10
            snake_length += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
