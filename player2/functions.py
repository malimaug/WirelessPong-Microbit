from microbit import *
import radio

def screen(data: dict):
    """It displays the right information on the LED matrix of the microbit depending on which players uses it

    Parameters
    ----------
    data: all the information needed to display
    """
    #get x values from player1 and 2
    x_player1 = data['x_player1']
    x_player2 = data['x_player2']
    x_ball = data['x_ball']
    y_ball = data['y_ball']

    display.clear()

    #display for player2

        #display player on screen
    display.set_pixel(x_player2, 4, 9)
    display.set_pixel(x_player2 + 1, 4 , 9)

    #if the ball is on the other side of the terrain then display the ball on the border
    if y_ball < 5:
        real_ball_y = 0
    else:
        real_ball_y = y_ball - 5

    # display the ball on screen
    display.set_pixel(x_ball,real_ball_y ,5)


def send_wireless_inputs():

    move = 0

    if button_a.was_pressed():
        move = -1

    if button_b.was_pressed():
        move = 1

    radio.send(str(move))


def get_wireless_data(data):

    try:
        info = radio.receive()
        if info[0] == '{':
            data = eval(info)
            keep_running = True

        elif info == 'end':
            data = data
            keep_running = False
    except:
        pass

    return data, keep_running