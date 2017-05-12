from __future__ import print_function
import httplib2
import os
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
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
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    #spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    spreadsheetId = '1SP7oeq_60bDXW4QbLZwDnzE_H9HlwIr41donZg_jS88'
    #rangeName = 'Class Data!A2:E'
    rangeName = 'Overall Leaderboard!A4:X'
    #rangeName = 'Import!D10:AF'    # Import tab in some of the tpl spreadsheets
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        output_json = 'TPLSeason05Stats.json'    
        #print('Name, Major:')
        with open(output_json, 'w') as outfile:
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4]))
                outfile.write("\n")
                outfile.write(str(row))

    # convert list into json
    '''output_json = 'output.json'
    with open(output_json, 'wb') as outfile:
        json.dumps(values, outfile)
    '''
if __name__ == '__main__':
    main()