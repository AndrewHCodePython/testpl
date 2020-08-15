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

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '16gLkJRHz3LoopHfz7UwCdzb2gOrIB1NsJkyavp82isY'
SAMPLE_RANGE_NAME = 'Overall Leaderboard!A4:X'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
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
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    
    output_json = "season_11.json"
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
    
    pp = pprint.PrettyPrinter(indent=4)

    if not values:
        print('No data found.')
    if len(values[0]) != 23:
        print("wrong number of rows: ", len(values[0]))
    else:
        for rows in values[1:]:
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
        
        pp.pprint(dictionary1)
    
    j = json.dumps(dictionary1, indent=4)
    f = open(output_json, 'w')
    f.write(j)
    f.close()

if __name__ == '__main__':
    main()