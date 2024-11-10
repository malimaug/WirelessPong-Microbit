from functions import *
from microbit import *
import radio



radio.config(channel=11)
radio.on()


def game():
    # setting up all positions for the different elements in the game
    player1, player2, ball = initialize_positions()
    game_is_running = True
    waiting = True

    starting_positions = package_game_positions(player1, player2, ball)

    #synchronise
    while waiting:
        radio.send('start')
        if radio.receive() == 'start_confirm':
            break

    #send starting positions
    radio.send(str(starting_positions))

    while game_is_running:


        #display on screen
        screen(player1, player2, ball)

        # check if players alive
        is_alive = check_if_alive(player1, player2, ball)

        if (not is_alive['player1']) or (not is_alive['player2']):
            game_is_running = False
            break

        # get players inputs
        player1 = get_inputs(player1)
        player2 = get_wireless_inputs(player2)

        # player movement
        player1, player2 = move_players(player1, player2)

        # ball movement
        ball = move_ball(player1, player2, ball)

        #send new data to player 2
        packed_data = package_game_positions(player1, player2, ball)
        radio.send(str(packed_data))

        sleep(500)

    # end game
    print("game over")
    display.scroll("game over")
    radio.send('end')


game()