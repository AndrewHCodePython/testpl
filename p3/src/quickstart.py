from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pprint
import json

# https://developers.google.com/sheets/api/quickstart/python

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def main():
    """
        TPL Season XVI - Myths and Legends  https://docs.google.com/spreadsheets/d/1N8kW89lcsU0iGxNm_KGHDWK9MDJ9bpwohlfaUUqMoW4/edit#gid=1238198717
        TPL Season XV - Video Games         https://docs.google.com/spreadsheets/d/1jU05zSqXXXnfnJwQQV8wq7Z2bdabnOXTHitOXLIeXxw/edit#gid=1238198717
        TPL Season XIV - Seinfeld           https://docs.google.com/spreadsheets/d/1F3wJvqe6naVQI4DWCTSBTQSBtLqaa54IYx91uf9yT_k/edit
        TPL Season XIII - Beer              https://docs.google.com/spreadsheets/d/1F3wJvqe6naVQI4DWCTSBTQSBtLqaa54IYx91uf9yT_k/edit#gid=1238198717
        TPL Season XII - Football           https://docs.google.com/spreadsheets/d/1d1mEl_2t7PBP71sdHD-N_Z-8wxEik8Th9lUO4-v0-Wk/edit?ts=5a733912#gid=1238198717
        TPL Season XI - Rom Com             https://docs.google.com/spreadsheets/d/16gLkJRHz3LoopHfz7UwCdzb2gOrIB1NsJkyavp82isY/edit#gid=1238198717
        TPL Season X - 80s Rockbands:       https://docs.google.com/spreadsheets/d/1K6fHhdBGHlyur1NTZ6ob0wEPAqjKMQSHPUwdlxglLa4/edit#gid=1238198717
        TPL Season IX - The Simpsons:       https://docs.google.com/spreadsheets/d/1qOVPR4Iiy0GSDczhO4gZMe0ZYKjiEx3e6iNBapBU1DQ/edit#gid=1238198717
        TPL Season VIII - 80s:              https://docs.google.com/spreadsheets/d/18OZCA7MDZ8-6ivja56pQjuxMSg8FV4W8GmVu01E6PH0/edit#gid=1238198717 
        TPL Season VII - Operation 007:     https://docs.google.com/spreadsheets/d/1THYcgYuOtX5sO9d9prG7ouwowAlfvpoGto1wgLK_7No/edit#gid=1238198717     
        TPL Season VI - Semester:           https://docs.google.com/spreadsheets/d/1SP7oeq_60bDXW4QbLZwDnzE_H9HlwIr41donZg_jS88/edit#gid=1238198717     
        TPL Season V:                       https://docs.google.com/spreadsheets/d/1qjGc2HD9yX4aHKtJRSn_D29N24F1IonLwG70krdT4PQ/edit#gid=1238198717 
        TPL Season IV:
        TPL Season III - GoT:               https://docs.google.com/spreadsheets/d/1AVBNISCLSvI-46OyLaLlw-dIkgEphXS535KEijZq1tY/edit#gid=1 
        TPL Season II:
        TPL Season I:
    """

    # parity related things
    output_json = "TPLSeason16Stats.json"
    dictionary1 = {}
    stat_keys = ['Salary', 
                'Goals', 
                'Assists', 
                '2nd Assists', 
                'Ds', 
                'Throwaways', 
                'Receiver Error', 
                'Wins', 
                'Times Traded', 
                'Ds:Turnover Ratio', 
                'Total Assist:Throw Away Ratio']
    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = '1N8kW89lcsU0iGxNm_KGHDWK9MDJ9bpwohlfaUUqMoW4'
    RANGE_NAME = 'Overall Leaderboard!A4:X'
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    credentials_path = '../../credentials/credentials.json'
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    
    pp = pprint.PrettyPrinter(indent=4)

    if not values:
        print('No data found.')
    if len(values[0]) != 23:
        print("wrong number of rows: ", len(values[0]))
    else:
        for rows in values[1:]:
            print(rows)
            for i in range(0, len(rows), 2):
                if rows[i] not in dictionary1:
                    # name = 'name: \"' + rows[i]
                    name = rows[i]
                    dictionary1[name] = {"Stats": dict.fromkeys(stat_keys)}
                if i == 0:
                    dictionary1[name]['Stats']['Salary'] = rows[i+1]
                if i == 2:
                    dictionary1[name]['Stats']['Goals'] = rows[i+1]
                if i == 4:
                    dictionary1[name]['Stats']['Assists'] = rows[i+1]
                if i == 6:
                    dictionary1[name]['Stats']['2nd Assists'] = rows[i+1]
                if i == 8:
                    dictionary1[name]['Stats']['Ds'] = rows[i+1]
                if i == 10:
                    dictionary1[name]['Stats']['Throwaways'] = rows[i+1]
                if i == 12:
                    dictionary1[name]['Stats']['Receiver Error'] = rows[i+1]
                if i == 14:
                    dictionary1[name]['Stats']['Wins'] = rows[i+1]
                if i == 16:
                    dictionary1[name]['Stats']['Times Traded'] = rows[i+1]
                if i == 18:
                    dictionary1[name]['Stats']['Ds:Turnover Ratio'] = rows[i+1]
                if i == 20:
                    dictionary1[name]['Stats']['Total Assist:Throw Away Ratio'] = rows[i+1]
        
        # pp.pprint(dictionary1)
    
    with open(output_json, 'w') as outfile:
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]))
                outfile.write("\n")
                outfile.write(str(row))

if __name__ == '__main__':
    main()