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


    while game_is_running:

        # debug section
        debug(player1, player2, ball, True, True)


        #Chooses which player's screen to display
        if is_player == 1:
            screen(player1, player2, ball, True)
        else:
            screen(player1, player2, ball, False)


        #check if players alive
        is_alive = check_if_alive(player1, player2, ball)

        if  (not is_alive['player1']) or (not is_alive['player2']):
            game_is_running = False
            break


        #player movement



        #ball movement
        ball = move_ball(player1, player2, ball)


        sleep(500)

    #end game
    print("game over")



game(2)

