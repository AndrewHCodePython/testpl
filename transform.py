#!/usr/bin/python 

import json
import pprint

dictionary1 = {}
stat_keys = ['Salary', 'Goals', 'Assists', '2nd Assists', 'Ds', 'Throwaways', 'Receiver Error', 'Wins', 'Times Traded', 'Ds:Turnover Ratio', 'Total Assist:Throw Away Ratio']

row1 = ['Cameron Dunning', '$830,500', 'Jeff Steele', '87', 'Chris Bracht', '72', 'Tom Jennings', '35', 'Greg Ellis', '36', 'Greg Ellis', '54', 'Taunya Tremblay', '0', 'Lawrence Wong', '10', 'James Irvine', '6', 'Kirk MacRae', '9.00', 'James Irvine', 'No TAs']
row2 = ['Jeff Steele', '$762,500', 'Tyler Curtis', '56', 'Cameron Dunning', '65', 'Carolina Vargas', '32', 'Miki Antonijevic', '28', 'Marcel Frenette-Corniellis', '41', 'Kirk MacRae', '0', 'KPL Lee', '9', 'Daniel Steinberg', '6', 'Chris Wang', '1.78', 'Alice Chung', '9.00']
row3 = ['Chris Bracht', '$778,500', 'Vikki Shimoda', '56', 'Jamie Dempster', '70', 'Greg Kramer', '33', 'Cameron Dunning', '36', 'BC Roedde', '54', 'Rajiv Seneviratne', '0', 'Miki Antonijevic', '9.5', 'Hin Tang', '6', 'Kate Jardine', '2.00', 'Kate Jardine', '10.67']
row4 = ['Greg Ellis', '$717,000', 'Meghan Janssen', '49', 'BC Roedde', '62', 'Ron Colon', '30', 'Cam Harris', '25', 'Greg Kramer', '40', 'Kevin Christensen', '0', 'Darrel Nantais', '9', 'Colin Thompson', '6', 'Mark Bustin', '1.67', 'Kirk MacRae', '8.00']
# for row1 in values (read from sheet) row1 is the rows[]

for i in range(0, len(row1), 2):
    if row1[i] not in dictionary1:
         dictionary1[row1[i]] = dict.fromkeys(stat_keys)

    if i == 0:
        dictionary1[row1[i]]['Salary'] = row1[i+1]
    if i == 2:
        dictionary1[row1[i]]['Goals'] = row1[i+1]
    if i == 4:
        dictionary1[row1[i]]['Assists'] = row1[i+1]
    if i == 6:
        dictionary1[row1[i]]['2nd Assists'] = row1[i+1]
    if i == 8:
        dictionary1[row1[i]]['Ds'] = row1[i+1]
    if i == 10:
        dictionary1[row1[i]]['Throwaways'] = row1[i+1]
    if i == 12:
        dictionary1[row1[i]]['Receiver Error'] = row1[i+1]
    if i == 14:
        dictionary1[row1[i]]['Wins'] = row1[i+1]
    if i == 16:
        dictionary1[row1[i]]['Times Traded'] = row1[i+1]
    if i == 18:
        dictionary1[row1[i]]['Ds:Turnover Ratio'] = row1[i+1]
    if i == 20:
        dictionary1[row1[i]]['Total Assist:Throw Away Ratio'] = row1[i+1]


for i in range(0, len(row2), 2):
    if row2[i] not in dictionary1:
        dictionary1[row2[i]] = dict.fromkeys(stat_keys)

    if i == 0:
        dictionary1[row2[i]]['Salary'] = row2[i+1]
    if i == 2:
        dictionary1[row2[i]]['Goals'] = row2[i+1]
    if i == 4:
        dictionary1[row2[i]]['Assists'] = row2[i+1]
    if i == 6:
        dictionary1[row2[i]]['2nd Assists'] = row2[i+1]
    if i == 8:
        dictionary1[row2[i]]['Ds'] = row2[i+1]
    if i == 10:
        dictionary1[row2[i]]['Throwaways'] = row2[i+1]
    if i == 12:
        dictionary1[row2[i]]['Receiver Error'] = row2[i+1]
    if i == 14:
        dictionary1[row2[i]]['Wins'] = row2[i+1]
    if i == 16:
        dictionary1[row2[i]]['Times Traded'] = row2[i+1]
    if i == 18:
        dictionary1[row2[i]]['Ds:Turnover Ratio'] = row2[i+1]
    if i == 20:
        dictionary1[row2[i]]['Total Assist:Throw Away Ratio'] = row2[i+1]


for i in range(0, len(row3), 2):
    if row3[i] not in dictionary1:
        dictionary1[row3[i]] = dict.fromkeys(stat_keys)

    if i == 0:
        dictionary1[row3[i]]['Salary'] = row3[i+1]
    if i == 2:
        dictionary1[row3[i]]['Goals'] = row3[i+1]
    if i == 4:
        dictionary1[row3[i]]['Assists'] = row3[i+1]
    if i == 6:
        dictionary1[row3[i]]['2nd Assists'] = row3[i+1]
    if i == 8:
        dictionary1[row3[i]]['Ds'] = row3[i+1]
    if i == 10:
        dictionary1[row3[i]]['Throwaways'] = row3[i+1]
    if i == 12:
        dictionary1[row3[i]]['Receiver Error'] = row3[i+1]
    if i == 14:
        dictionary1[row3[i]]['Wins'] = row3[i+1]
    if i == 16:
        dictionary1[row3[i]]['Times Traded'] = row3[i+1]
    if i == 18:
        dictionary1[row3[i]]['Ds:Turnover Ratio'] = row3[i+1]
    if i == 20:
        dictionary1[row3[i]]['Total Assist:Throw Away Ratio'] = row3[i+1]

for i in range(0, len(row4), 2):
    if row4[i] not in dictionary1:
        dictionary1[row4[i]] = dict.fromkeys(stat_keys)

    if i == 0:
        dictionary1[row4[i]]['Salary'] = row4[i+1]
    if i == 2:
        dictionary1[row4[i]]['Goals'] = row4[i+1]
    if i == 4:
        dictionary1[row4[i]]['Assists'] = row4[i+1]
    if i == 6:
        dictionary1[row4[i]]['2nd Assists'] = row4[i+1]
    if i == 8:
        dictionary1[row4[i]]['Ds'] = row4[i+1]
    if i == 10:
        dictionary1[row4[i]]['Throwaways'] = row4[i+1]
    if i == 12:
        dictionary1[row4[i]]['Receiver Error'] = row4[i+1]
    if i == 14:
        dictionary1[row4[i]]['Wins'] = row4[i+1]
    if i == 16:
        dictionary1[row4[i]]['Times Traded'] = row4[i+1]
    if i == 18:
        dictionary1[row4[i]]['Ds:Turnover Ratio'] = row4[i+1]
    if i == 20:
        dictionary1[row4[i]]['Total Assist:Throw Away Ratio'] = row4[i+1]

pprint.pprint(dictionary1)

# r = json.dumps(row1)

# with open('transform_data.json', 'w') as outfile:
#     json.dump(r, outfile)