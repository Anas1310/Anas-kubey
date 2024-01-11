import pygame 
import sys
from pygame import*

pygame.init()

#constants
width = 900
height = 800
disc_size = 80
#size of circles
row_amount = 5
column_amount = 7
yellow = (255, 255, 0)
red = (255, 0, 0)
empty = 0

screen = display.set_mode((width,height))

type_font = pygame.font.SysFont("Algerian", 60)
background = pygame.image.load("hidden-leaf-village.jpg")
background = pygame.transform.scale(background, (width, height))

def draw_text(text, font, colour, x, y):
    image = font.render(text, True, colour)
    screen.blit(image, (x, y))
    return image

def make_empty_counter():
    board = []
    row_worth = 0
    while row_worth < row_amount:
        board.append([empty] * column_amount)
        row_worth = row_worth + 1
    return board

def drop_token(board, col, player):
    row = row_amount - 1


    while row >= 0 and board[row][col] != empty:
        row = row - 1

    if row >= 0:
        board[row][col] = player
        return True
    else:
        return False
def draw_board(screen, board):
  row = 0

  while row < row_amount:
      col = 0
      while col < column_amount:
          x = col * disc_size + 198
          y = row * disc_size + 400
          pygame.draw.circle(screen, (255, 255, 255), (x, y), 30)

          if board[row][col] == 1:
              pygame.draw.circle(screen, red, (x, y), 30)
          elif board[row][col] == 2:
              pygame.draw.circle(screen, yellow, (x, y), 30)

          col += 1

      row += 1

def draw_display_board(screen):
        x = 140
        y = 290
        width = 600
        height = 500
        pygame.draw.rect(screen, (31, 182, 255), (x, y, width, height))

current_player = 1
game_board = make_empty_counter()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            col = (event.pos[0] - 198) // disc_size 

            if 0 <= col < column_amount and drop_token(game_board, col, current_player):
                current_player = 3 - current_player

    screen.blit(background, (0, 0))  # Draw the background image

    draw_text("Connect 4", type_font, (0, 0, 0), 100, 100)


    draw_display_board(screen)
    draw_board(screen, game_board)

    time.delay(5)
    display.flip()