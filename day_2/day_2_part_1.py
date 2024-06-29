# https://adventofcode.com/2023/day/2

import re

game_records = open('input.txt', 'r')

red_max = 12
green_max = 13
blue_max = 14

possible_games = []

def game_number(game):
    # strip everything except the game number
    game_num = game.split(":")[0]
    return re.sub(r'\D', '', game_num)

def color_check(colors):
    # compare color count to available colors
    for color in colors:
        if "red" in color and int(re.sub(r'\D', '', color)) > red_max:
            return False
        if "green" in color and int(re.sub(r'\D', '', color)) > green_max:
            return False
        if "blue" in color and int(re.sub(r'\D', '', color)) > blue_max:
            return False 
    return True

def game_check(file):
    for line in file:
        line = line.rstrip('\n')
        game_num = game_number(line)
        
        colors = line.split(":")[1].replace(";", ",").split(",")
        valid_game = color_check(colors)

        if valid_game:
            possible_games.append(int(game_num))
        else:
            pass

game_check(game_records)
print (sum(possible_games))