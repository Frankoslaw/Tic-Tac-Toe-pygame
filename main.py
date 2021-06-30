import pygame

pygame.init()

WIDTH = 500
ROWS = 3
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe with pygame by Franciszek Łopuszański")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

X_IMAGE = pygame.transform.scale(pygame.image.load("cross.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("circle.png"), (150, 150))

END_FONT = pygame.font.SysFont('courier', 40)


def draw_grid():
    gap = WIDTH // ROWS

    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap

        pygame.draw.line(win, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(win, GRAY, (0, x), (WIDTH, x), 3)


def initialize_grid():
    game_array = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

    return game_array


def click(game_array):
    global x_turn, images

    m_x, m_y = pygame.mouse.get_pos()

    x_field = m_x // (WIDTH // ROWS)
    y_field = m_y // (WIDTH // ROWS)

    image = X_IMAGE if x_turn else O_IMAGE
    images.append((x_field * (WIDTH // ROWS) + 75, y_field * (WIDTH // ROWS) + 75, image))
    char = 'X' if x_turn else 'O'
    game_array[y_field][x_field] = char
    x_turn = not x_turn


def has_won(game_array):
    for i in range(3):
        if(game_array[0][i] == game_array[1][i] == game_array[2][i] != " "):
            display_message(game_array[2][i] + " has won!")
            return True

        if(game_array[i][0] == game_array[i][1] == game_array[i][2] != " "):
            display_message(game_array[i][2] + " has won!")
            return True

    if (game_array[0][0] == game_array[1][1] == game_array[2][2]  != " "):
        display_message(game_array[2][2] + " has won!")
        return True

    if (game_array[0][2] == game_array[1][1] == game_array[2][0] != " "):
        display_message(game_array[2][0] + " has won!")
        return True

    return False

def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j] == " ":
                return False

    display_message("It's a draw!")
    return True


def display_message(content):
    pygame.time.delay(500)
    win.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def render():
    win.fill(WHITE)
    draw_grid()

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def main():
    global x_turn, images, draw

    images = []
    draw = False

    run = True

    x_turn = True

    game_array = initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        if has_won(game_array) or has_drawn(game_array):
            run = False


while True:
    if __name__ == '__main__':
        main()