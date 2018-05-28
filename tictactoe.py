import pygame
from pygame.locals import *

# global variables
XO = "X"  # x goes allways first
table = [[None, None, None], \
        [None, None, None], \
        [None, None, None]]

winner = None


#functions

def initGame(myGame):
    # myGame : typical pygame backround used for tictactoe game
    # used pygame.org backround example
    background = pygame.Surface(myGame.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    # table vert lines...
    pygame.draw.line(background, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(background, (0, 0, 0), (200, 0), (200, 300), 2)

    # table horiz lines...
    pygame.draw.line(background, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(background, (0, 0, 0), (0, 200), (300, 200), 2)

    return background


def drawStatus(game):
    # status messages: whos turn, who won

    # access for global variables
    global XO, winner

    # status messages
    if (winner is None):
        message = XO + "'s turn"
    else:
        message = winner + " won!"

    font = pygame.font.Font(None, 25)
    text = font.render(message, 1, (10, 10, 10))

    game.fill((250, 250, 250), (0, 300, 300, 25))
    game.blit(text, (10, 300))


def showGame(myGame, game):
    # myGame: the initialized pyGame display
    # game:   the game board surface

    drawStatus(game)
    myGame.blit(game, (0, 0))
    pygame.display.flip()

def mouseMove(userX, userY):
    # userX : user with X
    # userY : user with O

    # for row
    if (userY < 100):
        row = 0
    elif (userY < 200):
        row = 1
    else:
        row = 2

    # for column
    if (userX < 100):
        col = 0
    elif (userX < 200):
        col = 1
    else:
        col = 2

    return (row, col)


def drawMove(game, tableRow, tableCol, element):

    # determine the center of the square
    colcentX = ((tableCol) * 100) + 50
    rowcentY = ((tableRow) * 100) + 50

    # elements : X and O
    if (element == 'O'):
        pygame.draw.circle(game, (0, 0, 0), (colcentX, rowcentY), 44, 2)
    else:
        pygame.draw.line(game, (0, 0, 0), (colcentX - 22, rowcentY - 22), \
                         (colcentX + 22, rowcentY + 22), 2)
        pygame.draw.line(game, (0, 0, 0), (colcentX + 22, rowcentY - 22), \
                         (colcentX - 22, rowcentY + 22), 2)

    # mark the space as used
    table[tableRow][tableCol] = element


def clickTable(game):

    global table, XO

    (userX, userY) = pygame.mouse.get_pos()
    (row, col) = mouseMove(userX, userY)

    # make sure space is empty
    if ((table[row][col] == "X") or (table[row][col] == "O")):
        # this space is in use
        return

    # use X or O
    drawMove(game, row, col, XO)

    # enter second user move
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"


def gameWinner(game):
    # find winner
    global table, winner

    # rows
    for row in range(0, 3):
        if ((table[row][0] == table[row][1] == table[row][2]) and \
                (table[row][0] is not None)):
            # winner
            winner = table[row][0]
            pygame.draw.line(game, (250, 0, 0), (0, (row + 1) * 100 - 50), \
                             (300, (row + 1) * 100 - 50), 2)
            break

    # columns
    for col in range(0, 3):
        if (table[0][col] == table[1][col] == table[2][col]) and \
                (table[0][col] is not None):
            # winner
            winner = table[0][col]
            pygame.draw.line(game, (250, 0, 0), ((col + 1) * 100 - 50, 0), \
                             ((col + 1) * 100 - 50, 300), 2)
            break

    # diagonal win
    if (table[0][0] == table[1][1] == table[2][2]) and \
            (table[0][0] is not None):
        # winner left to right
        winner = table[0][0]
        pygame.draw.line(game, (250, 0, 0), (50, 50), (250, 250), 2)

    if (table[0][2] == table[1][1] == table[2][0]) and \
            (table[0][2] is not None):
        # winner right to left
        winner = table[0][2]
        pygame.draw.line(game, (250, 0, 0), (250, 50), (50, 250), 2)
# --------------------------------------------------------------------
# Settings
pygame.init()
myGame = pygame.display.set_mode((300, 325))

# create the table
game = initGame(myGame)

# main loop
running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            # after click place X or O
            clickTable(game)

        # check winner
        gameWinner(game)

        # update the display
        showGame(myGame, game)
