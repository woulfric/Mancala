from game import *
from Variables import *
import time
pygame.init()

board = MancalaBoard()
game = Game(board, -1)
 

next_player = 2
while(not game.gameOver()):

    # next_player = Play.humanTurn(game, next_player)
    next_player, game = Play.computerTurn(game, next_player)
    Play.computerTurn(game, 1)

    window.fill(BG_Color)
    game.state.draw()
    pygame.display.flip()
    time.sleep(0.2)

window.fill(BG_Color)
game.state.draw()
# time.sleep(10)

if game.gameOver():
    print("the game is over")

window.fill(BG_Color)
game.state.draw()


winner, score = game.findWinner()
print("Player ",winner,"won, with ",score,"points")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

