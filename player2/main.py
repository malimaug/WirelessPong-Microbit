from functions import *
from microbit import *
import radio

radio.config(channel=11)
radio.on()

def game():

    waiting = True
    game_running = True


    #synchrosnise
    while waiting:
        if radio.receive() == 'start':
            radio.send('start_confirm')
            sleep(10)
            break

    data = eval(radio.receive())

    while game_running:

        #display on screen
        screen(data)

        #receive data
        data, game_running = get_wireless_data(data)

        #detect and send inputs
        send_wireless_inputs()

    print('game over')
    display.scroll('game over')

game()