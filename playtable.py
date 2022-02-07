import pygame
import sys
import random

size_block = 60
margin = 6
width = heigth = size_block * 10 + margin * 11

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("tic-tac-toe")

colour_cell = {'RED': (255, 0, 0), 'BLUE': (0, 0, 255), 'GRAY': (220, 220, 220), 'WHITE': (255, 255, 255),
               'BLACK': (0, 0, 0)}
gametable = [[0] * 10 for i in range(10)]
query = 1
game_over = False


def check_win(gametable, sign):
    zeroes = 0

    for row in gametable: #проверка свободных ячеек
        zeroes += row.count(0)

    for row in range(10): #горизонтальная проверерка
        for column in range(6):
            if gametable[row][column] == sign and gametable[row][column + 1] == sign and gametable[row][
                column + 2] == sign and \
                    gametable[row][column + 3] == sign and gametable[row][column + 4] == sign:
                return sign

    for row in range(6): #вертикальная проверка
        for column in range(10):
            if gametable[row][column] == sign and gametable[row + 1][column] == sign and gametable[row + 2][
                column] == sign and \
                    gametable[row + 3][column] == sign and gametable[row + 4][column] == sign:
                return sign

    for row in range(6): #горизонтальная проверка
        for column in range(6):
            if gametable[row][column] == sign and gametable[row + 1][column + 1] == sign and gametable[row + 2][
                column + 2] == sign and \
                    gametable[row + 3][column + 3] == sign and gametable[row + 4][column + 4] == sign:
                return sign

    for row in range(6):
        for column in (range(4, 10)):
            if gametable[row][column] == sign and gametable[row + 1][column - 1] == sign and gametable[row + 2][
                column - 2] == sign and \
                    gametable[row + 3][column - 3] == sign and gametable[row + 4][column - 4] == sign:
                return sign

    if zeroes == 0:
        return 'draw'

    return False


def check_event():
    global query, game_over, gametable
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #закрыть игру
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over and query % 2 == 1: #левый клик
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if gametable[row][column] == 0:
                gametable[row][column] = 'x'
                query += 1

        elif query % 2 == 0 and not game_over: #ход компа
            ai()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #правый клик
            game_over = False
            gametable = [[0] * 10 for i in range(10)]
            query = 1
            screen.fill(colour_cell['BLACK'])


def draw_table():
    global game_over, gametable, query
    if not game_over:
        for column in range(10):
            for row in range(10):
                if gametable[row][column] == 'x':
                    colour = colour_cell['RED']
                elif gametable[row][column] == 'o':
                    colour = colour_cell['BLUE']
                else:
                    colour = colour_cell['GRAY']
                x = column * size_block + (column + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, colour, (x, y, size_block, size_block))
                if colour == colour_cell['RED']:
                    pygame.draw.line(screen, colour_cell['WHITE'], (x + 5, y + 5),
                                     (x + size_block - 5, y + size_block - 5),
                                     5)
                    pygame.draw.line(screen, colour_cell['WHITE'], (x + size_block - 5, y + 5),
                                     (x + 5, y + size_block - 5),
                                     5)
                elif colour == colour_cell['BLUE']:
                    pygame.draw.circle(screen, colour_cell['WHITE'], (x + size_block // 2, y + size_block // 2),
                                       size_block // 2 - 3, 4)

    if query % 2 == 0:
        game_over = check_win(gametable, 'x')
    else:
        game_over = check_win(gametable, 'o')

    if game_over:
        screen.fill(colour_cell['BLACK'])
        font = pygame.font.SysFont('stxingkai', 80)
        texts = font.render(game_over, True, colour_cell['WHITE'])
        text_rect = texts.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(texts, [text_x, text_y])

    pygame.display.update()


def ai(): #бот с тактикой тыка
    global query, gametable, game_over
    if query % 2 == 0:
        random_x = random.randint(90, 900) // 100
        random_y = random.randint(90, 900) // 100
        if gametable[random_x][random_y] == 0:
            gametable[random_x][random_y] = 'o'
            query += 1
