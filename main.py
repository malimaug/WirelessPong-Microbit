from functions import *


"""
 43210 player1
0--##-4
1-----3
2-----2
3-----1
4-----0
.01234.virtual index
5-----0
6-----1
7-----2
8-----3
9--##-4
 01234 player2
"""




def game(is_player: int):

    #setting up all positions for the different elements in the game
    player1, player2, ball = initialize_positions()
    game_is_running = True

    #debug section
    game_state = package_game_positions(player1, player2, ball)
    debug(game_state, True)


    while game_is_running:

        #check if players alive
        is_alive = check_if_alive(player1, player2, ball)

        if  not is_alive['player1'] and not is_alive['player2']:
            game_is_running = False


        #Chooses which player's screen to display
        if is_player == 1:
            screen(player1, player2, ball, True)
        else:
            screen(player1, player2, ball, False)


        #player movement



        #ball movement
        ball = ball_move(player1, player2, ball)

        sleep(500)

    #end game
    print("game over")



game(2)

