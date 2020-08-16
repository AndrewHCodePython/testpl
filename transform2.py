#!/usr/bin/python 

import json
import pprint

sheet_columns = ['Salary', 'Goals', 'Assists', '2nd Assists', 'Ds', 'Throwaways', 'Receiver Error', 'Wins', 'Times Traded', 'Ds:Turnover Ratio', 'Total Assist:Throw Away Ratio']
stats_keys = ['salary', 'goals', 'assists', 'secondAssists', 'ds', 'throwaways', 'receiverError', 'wins', 'timesTraded', 'dTurnoverRatio', 'assistThrowawayRatio']
all_players = {}
file_ext = ".json"

file_prefix = "TPLSeason16Stats"
season_name = "Myths & Legends"
season_id = 16

input_file = file_prefix + file_ext
output_file_name = file_prefix + "Transformed" + file_ext

row1 = ['Cameron Dunning', '$830,500', 'Jeff Steele', '87', 'Chris Bracht', '72', 'Tom Jennings', '35', 'Greg Ellis', '36', 'Greg Ellis', '54', 'Taunya Tremblay', '0', 'Lawrence Wong', '10', 'James Irvine', '6', 'Kirk MacRae', '9.00', 'James Irvine', 'No TAs']
row2 = ['Jeff Steele', '$762,500', 'Tyler Curtis', '56', 'Cameron Dunning', '65', 'Carolina Vargas', '32', 'Miki Antonijevic', '28', 'Marcel Frenette-Corniellis', '41', 'Kirk MacRae', '0', 'KPL Lee', '9', 'Daniel Steinberg', '6', 'Chris Wang', '1.78', 'Alice Chung', '9.00']
row3 = ['Chris Bracht', '$778,500', 'Vikki Shimoda', '56', 'Jamie Dempster', '70', 'Greg Kramer', '33', 'Cameron Dunning', '36', 'BC Roedde', '54', 'Rajiv Seneviratne', '0', 'Miki Antonijevic', '9.5', 'Hin Tang', '6', 'Kate Jardine', '2.00', 'Kate Jardine', '10.67']
row4 = ['Greg Ellis', '$717,000', 'Meghan Janssen', '49', 'BC Roedde', '62', 'Ron Colon', '30', 'Cam Harris', '25', 'Greg Kramer', '40', 'Kevin Christensen', '0', 'Darrel Nantais', '9', 'Colin Thompson', '6', 'Mark Bustin', '1.67', 'Kirk MacRae', '8.00']

def create_player():
    stats_dict = dict.fromkeys(stats_keys)
    player_dict = dict({
        'name': None,
        'stats': stats_dict,
        'zuluruId': 0,
        'sex': ""
    })

    return player_dict

def readFromFile(input_file):
    file = "./stats/rawdata/" + input_file
    f = open(file, 'r')
    output = f.readlines()
    f.close()

    return output

def cleanse(input_lines):
    # remove first two rows in array
    input_lines.pop(0)
    input_lines.pop(0)

    for i in range(0, len(input_lines)):
        # trim the first and last square bracket
        # input_lines[i] = input_lines[i][1:-1]
        
        # remove ALL single quotes
        input_lines[i] = input_lines[i].replace("[", "")
        input_lines[i] = input_lines[i].replace("]", "")
        input_lines[i] = input_lines[i].replace("'", "")

    return input_lines

lines = readFromFile(input_file)
cleansed_input = cleanse(lines)

# go every second element (to find the name)
for j in range(2, len(cleansed_input)):
    row = cleansed_input[j].split(", ")
    for i in range(0, len(row), 2):
        # print(row[i] + "\n")
        if row[i] not in all_players:
            player_dict = create_player()
            player_dict['name'] = row[i]
            all_players[row[i]] = player_dict
        
        # populate the salary (python doesn't have switch case staements)
        if (i == 0):
            all_players[row[i]]['stats']['salary'] = row[i+1]
            print(row[i])
            print(all_players[row[i]])

        if (i == 2):
            all_players[row[i]]['stats']['goals'] = row[i+1]
            print(row[i])
            print(all_players[row[i]])
        
        if (i == 4):
            all_players[row[i]]['stats']['assists'] = row[i+1]

        if (i == 6):
            all_players[row[i]]['stats']['secondAssists'] = row[i+1]

        if (i == 8):
            all_players[row[i]]['stats']['ds'] = row[i+1]

        if (i == 10):
            all_players[row[i]]['stats']['throwaways'] = row[i+1]
            
        if (i == 12):
            all_players[row[i]]['stats']['receiverError'] = row[i+1]

        if (i == 14):
            all_players[row[i]]['stats']['wins'] = row[i+1]

        if (i == 16):
            all_players[row[i]]['stats']['timesTraded'] = row[i+1]

        if (i == 18):
            all_players[row[i]]['stats']['dTurnoverRatio'] = row[i+1]
        
        if (i == 20):
            all_players[row[i]]['stats']['assistThrowawayRatio'] = row[i+1]
        
        all_players[row[i]]['stats']['season'] = season_name
        all_players[row[i]]['stats']['seasonId'] = season_id


# convert dictionary into list
list_players = [ p for p in all_players.values() ]

with open("stats/transformeddata/" + output_file_name, "w") as outfile:
    json.dump(list_players, outfile, indent=4, sort_keys=True)