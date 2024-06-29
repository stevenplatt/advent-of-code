# https://adventofcode.com/2023/day/2#part2

import re

game_records = open('input.txt', 'r')
total_power = []

def game_number(game):
    # strip everything except the game number
    game_num = game.split(":")[0]
    return re.sub(r'\D', '', game_num)

# pending
def game_power(colors):
    red_max = 0
    green_max = 0
    blue_max = 0

    calculated_power = 0

    # set max for each color
    for color in colors:
        color_val = int(re.sub(r'\D', '', color))
        if "red" in color and color_val > red_max:
            red_max = color_val
        if "green" in color and color_val > green_max:
            green_max = color_val
        if "blue" in color and color_val > blue_max:
            blue_max = color_val
    
    return (red_max * green_max * blue_max)

def load_games(file):
    for line in file:
        line = line.rstrip('\n')
        game_num = game_number(line)
        
        colors = line.split(":")[1].replace(";", ",").split(",")
        total_power.append(int(game_power(colors))) 

load_games(game_records)
print (sum(total_power))