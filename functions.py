from microbit import *
import random

def screen(player1: dict, player2: dict, ball: dict, is_player1: bool):
    """It displays the right information on the LED matrix of the microbit depending on which players uses it

    Parameters
    ----------
    player1 : player1's data (dict)
    player2 : player2's data (dict)
    ball: the dictionary containing all the ball's data (dict)
    is_player1 : True if the display is supposed to display the player1 screen, False if it supposed to display the player2 screen (bool)
    """
    #get x values from player1 and 2
    x_player1 = player1['x']
    x_player2 = player2['x']

    display.clear()

    #display for player1
    if is_player1:

        #conversion variables from the virtual terrain to the possible display
        virtual_coordinates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        real_coordinates = [4, 3, 2, 1, 0]

        #converts player coordinates from virtual to real
        x_index_player = virtual_coordinates.index(x_player1)

        #display player on screen
        display.set_pixel(real_coordinates[x_index_player], 4, 9)
        display.set_pixel(real_coordinates[x_index_player]+1, 4, 9)

        #converts ball coordinates from virtual to real
        x_index_ball = virtual_coordinates.index(ball['x'])
        real_ball_x = real_coordinates[x_index_ball]
        y_index_ball = virtual_coordinates.index(ball['y'])

        #if the ball is on the other side of the terrain then display the ball on the border
        if ball['y'] > 4:
            real_ball_y = 0
        else:
            real_ball_y = real_coordinates[y_index_ball]

        #display the ball on screen
        display.set_pixel(real_ball_x, real_ball_y, 5)

    #display for player2
    else:

        #display player on screen
        display.set_pixel(x_player2, 4, 9)
        display.set_pixel(x_player2 + 1, 4 , 9)

        #if the ball is on the other side of the terrain then display the ball on the border
        if ball['y'] < 5:
            real_ball_y = 0
        else:
            real_ball_y = ball['y'] - 5

        # display the ball on screen
        display.set_pixel(ball['x'],real_ball_y ,5)


def initialize_positions():
    """
    It gives all the starting positions to both players and the ball + the ball speed

    Returns
    -------
    player1 :  a dictionary containing player1's position, and it's score (dict)
    player2 :  a dictionary containing player2's position, and it's score (dict)
    ball: a dictionary containing all the ball's data (dict)
    """
    player1 = {'x': 2, 'score': 0}
    player2 = {'x': 2, 'score': 0}

    y_ball = random.randint(4, 5)
    ball = {'x': 2,
            'y': y_ball,
            'direction_x': 0,
            'direction_y': -1 if y_ball == 4 else 1,
            'speed': 13,
            'next_move_in': 13}

    return player1, player2, ball


def package_game_positions(player1: dict, player2: dict, ball: dict) -> dict:
    """
    The function packages all the positions into a form that the debug function uses

    Parameters
    ----------
    player1 : player1's data (dict)
    player2 : player2's data (dict)
    ball: ball's data (dict)

    Returns
    ------
    all_positions: the dictionary containing all the positions of all the objects in the game
    """
    #get x values from player1 and 2
    x_player1 = player1['x']
    x_player2 = player2['x']

    #package the data
    all_positions = {"x_player1": x_player1, "x_player2": x_player2, "x_ball": ball['x'], 'y_ball': ball['y']}
    return all_positions


def debug(player1: dict, player2: dict, ball: dict, print_virtual_terrain: bool = False, print_ball_data: bool = False):
    """
    The function allows the use for different debuging tools

    Parameters
    ----------
    player1 : player1's data (dict)
    player2 : player2's data (dict)
    ball: ball's data (dict)
    print_virtual_terrain : allows the function to print the virtual terrain in the console (bool)
    print_ball_data: allows the function to print the ball's data in the console (bool)
    """

    if print_ball_data:
        info = "Ball data: %s" % ball
        print("-"*(len(info) // 3))
        print(info)
        print("-"*(len(info) // 3)+'\n')


    if print_virtual_terrain:

        #puts all position data together
        game_positions = package_game_positions(player1, player2, ball)

        #creates the terrain table
        terrain = [["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"]]

        #adds the player1 positions
        terrain[game_positions["x_player1"]][0] = "#"
        terrain[game_positions["x_player1"] - 1 ][0] = "#"

        #adds the player2 positions
        terrain[game_positions["x_player2"]][9] = "#"
        terrain[game_positions["x_player2"] + 1 ][9] = "#"

        #adds the ball position
        terrain[game_positions["x_ball"]][game_positions["y_ball"]] = "@"

        #display in console
        print("Debug: virtual_terrain")
        print("-----"*5)
        print(" 01234")
        for y in range(0, 10):

            line = "%d" %y
            for x in range(0, 5):
                line += terrain[x][y]

            print(line)


def move_ball(player1: dict, player2: dict, ball: dict) -> dict:
    """Updates the dict ball for it to be able to move

    Parameters
    ----------
    player1 : player1's data (dict)
    player2 : player2's data (dict)
    ball: the data we want to update (dict)

    Returns
    -------
    new_ball: the updated dict (dict)

    """
    #get x values from player1 and 2
    x_player1 = player1['x']
    x_player2 = player2['x']

    # keep direction unless any of the following conditions are right
    new_direction_x = ball['direction_x']
    new_direction_y = ball['direction_y']

    # left side player1 paddle bounce
    if ball['x'] == x_player1 and ball['y'] == 0:
        new_direction_x = 1
        new_direction_y = -ball['direction_y']

    # right side player1 paddle bounce
    elif ball['x'] == x_player1 - 1 and ball['y'] == 0:
        new_direction_y = -1
        new_direction_y = -ball['direction_y']

    # left side player2 bounce
    if ball['x'] == x_player2 and ball['y'] == 9:
        new_direction_x = -1
        new_direction_y = -ball['direction_y']

    # right side player2 bounce
    if ball['x'] == x_player2 + 1 and ball['y'] == 9:
        new_direction_x = 1
        new_direction_y = -ball['direction_y']

    # bounce on side of the screen
    if ball['x'] == 4 or ball['x'] == 0:
        new_direction_x = -ball['direction_x']

    if ball['y'] == 9 or ball['y'] == 0:
        new_direction_y = -ball['direction_y']

    new_x = ball['x'] + new_direction_x
    new_y = ball['y'] + new_direction_y

    new_ball = {"x": new_x,
                "y": new_y,
                "direction_x": new_direction_x,
                "direction_y": new_direction_y,
                "speed": ball['speed'],
                "next_move_in": ball['next_move_in']}

    return new_ball


def check_if_alive(player1: dict, player2: dict, ball: dict) -> dict:
    """Tells if the given player is still alive

    Parameters
    ----------
    player1 : player1's data (dict)
    player2 : player2's data (dict)'
    ball : ball's data (dict)

    Returns
    -------
    result: assigns for each player if it is alive/True or not/False (dict)

    """
    # get x values from player1 and 2
    x_player1 = player1['x']
    x_player2 = player2['x']

    # initialize return dictionary (by default everyone is alive)
    result = {'player1': True, 'player2': True}

    # check if player1 is dead
    if x_player1 != ball['x'] and x_player1 - 1 != ball['x'] and ball['y'] == 0:
        result['player1'] = False

    # check if player2 is dead
    if x_player2 != ball['x'] and x_player2 + 1 != ball['x'] and ball['y'] == 9:
        result['player2'] = False


    return result