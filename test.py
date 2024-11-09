from functions import *

player1, player2, ball = initialize_positions()

# debug section
game_positions = package_game_positions(player1, player2, ball)
debug(game_positions, True)