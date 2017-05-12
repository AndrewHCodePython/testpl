import os
import json
import pprint 


json_data = {
    "Parity Season": "TPL Season 10 - Rock Bands: Public Doc",
    "Players": [{
            "Name": "Normal Lew",
                "Stats":{
                    "Wins": "7",
                    "Times Traded": "2",
                    "Receiver Error": "7",
                    "Goals": "30",
                    "2nd Assists": "25",
                    "Total Assist:Throw Away Ratio": "2.38",
                    "Ds:Turnover Ratio": "0.55",
                    "Throwaways": "40",
                    "Salary": "$679,000",
                    "Ds": "26",
                    "Assists": "70"
                }
        },
        {
            "Name": "David Ip",
                "Stats": {
                    "Wins": "7",
                    "Times Traded": "1",
                    "Receiver Error": "1",
                    "Goals": "42",
                    "2nd Assists": "14",
                    "Total Assist:Throw Away Ratio": "1.57",
                    "Ds:Turnover Ratio": "0.50",
                    "Throwaways": "21",
                    "Salary": "$460,500",
                    "Ds": "11",
                    "Assists": "19"
                }
            },
        {
            "Name": "Taunya Tremblay", 
                "Stats": {
                    "Wins": "2",
                    "Times Traded": "1",
                    "Receiver Error": "1",
                    "Goals": "7",
                    "2nd Assists": "6",
                    "Total Assist:Throw Away Ratio": "7.00",
                    "Ds:Turnover Ratio": "1.00",
                    "Throwaways": "1",
                    "Salary": "$171,500",
                    "Ds": "2",
                    "Assists": "1"
                }
            },
        {
            "Name": "Remi Jr. Ojo",
                "Stats": {
                    "Wins": "7",
                    "Times Traded": "0",
                    "Receiver Error": "5",
                    "Goals": "46",
                    "2nd Assists": "17",
                    "Total Assist:Throw Away Ratio": "2.24",
                    "Ds:Turnover Ratio": "0.54",
                    "Throwaways": "34",
                    "Salary": "$682,000",
                    "Ds": "21",
                    "Assists": "59"
                }
        },
        {
            "Name": "Mathew Harder",
                "Stats": {
                    "Wins": "6.5",
                    "Times Traded": "4",
                    "Receiver Error": "2",
                    "Goals": "7",
                    "2nd Assists": "21",
                    "Total Assist:Throw Away Ratio": "4.43",
                    "Ds:Turnover Ratio": "0.78",
                    "Throwaways": "7",
                    "Salary": "$285,000",
                    "Ds": "7",
                    "Assists": "10"
            }
        },
        {
            "Name": "Finlay D'silva",
                "Stats": {
                    "Wins": "4.5",
                    "Times Traded": "1",
                    "Receiver Error": "2",
                    "Goals": "9",
                    "2nd Assists": "25",
                    "Total Assist:Throw Away Ratio": "2.11",
                    "Ds:Turnover Ratio": "0.10",
                    "Throwaways": "28",
                    "Salary": "$323,500",
                    "Ds": "3",
                    "Assists": "34"
                }
        }
    ]
}

print(json_data['Parity Season'])
print("==================================================")
print(json_data['Players'])
print("==================================================")
name = "Finlay D\'silva"
player = json_data['Players'][name]['Name']
stats = json_data['Players'][0]['Stats']
print (player)
print(stats)


json_data2 = {
    "Parity Season": "TPL Season 10 - Rock Bands: Public Doc",
    "Darrel Nantais": {
        "Ds:Turnover Ratio": "0.33",
        "Goals": "5",
        "Receiver Error": "0",
        "2nd Assists": "37",
        "Assists": "60",
        "Wins": "5.5",
        "Total Assist:Throw Away Ratio": "1.87",
        "Times Traded": "0",
        "Ds": "17",
        "Throwaways": "52",
        "Salary": "$466,500"
    },
    "Matthew Colphon": {
        "Ds:Turnover Ratio": "0.83",
        "Goals": "34",
        "Receiver Error": "4",
        "2nd Assists": "6",
        "Assists": "7",
        "Wins": "4.5",
        "Total Assist:Throw Away Ratio": "0.93",
        "Times Traded": "3",
        "Ds": "15",
        "Throwaways": "14",
        "Salary": "$359,500"
    },
    "Danielle Leung": {
        "Stats":{
            "Ds:Turnover Ratio": "0.68",
            "Goals": "23",
            "Receiver Error": "3",
            "2nd Assists": "15",
            "Assists": "9",
            "Wins": "9.5",
            "Total Assist:Throw Away Ratio": "1.50",
            "Times Traded": "2",
            "Ds": "13",
            "Throwaways": "16",
            "Salary": "$352,500"
        }
    }
}

print(json_data2['Parity Season'])
print("==================================================")
player = 'Darrel Nantais'
print(json_data2[player])
print(json_data2[player]['Goals'])
print("==================================================")
player = 'Danielle Leung'
print(json_data2[player])
print(json_data2[player]['Stats'])
print(json_data2[player]['Stats']['Goals'])
