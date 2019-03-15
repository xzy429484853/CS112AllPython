from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^dont touch imports
import getpass  # for input hiding

'''
for push to spreadsheet stuff below
'''
from pprint import pprint
#what is this stuff below for?
# from googleapiclient import discovery



try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly' #read only acces to sheets
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'  # read/write access to sheets
# CLIENT_SECRET_FILE = 'client_id.json'
CLIENT_SECRET_FILE = 'client_id.json'
APPLICATION_NAME = 'GMU MIX card reader'

#dont touch this stuff
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
    # credential_path = os.path.join(credential_dir,'sheets.googleapis.com-python-quickstart.json')
    credential_path = os.path.join(credential_dir, 'mail_to_g_app.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^DONT FUCKING TOUCH above stuff
def main():
    """Shows basic usage of the Sheets API.

    Change below details as needed to access desired spreadsheet"""
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
    #Change line below to desired spreadsheet name ID found in the URL of the spreadsheet
    #spreadsheetId = '1Ts7Kca8y-Bwbf5Hlqj5gLA-GZeFXoLleZLC7NVYLohQ'  # placeholder birthday sheet
    spreadsheetId = '1K3d3hhZIdM4Oj_ev6KEMHu31a66KzdzxQF4p4Swj56M' #Database Spreadsheet
	#spreadsheetId = '1klI6NPddst_eBgqOeEBP7qydzqphjUd8g9EkrOxY7TQ' #Car Mileage Spreadsheet // My Drive home

    a_val = 1
    c_val = 5
    #change rangename file name
    filename = 'Sheet2'
    startcol = 'A'
    endcol = 'C'
    rangeName = filename+ '!'+ startcol + str(a_val) + ':'+ endcol + str(c_val)

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    print(values)

    '''
    if not values:
        print('No data found.')
    else:
        #print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 1 2.
            print('%s, %s, %s' % (row[0],row[1],row[2]))
    '''
    swipe = getpass.getpass(prompt='Please swipe: ', stream=None)

    '''
    print(values)
    if values[1][2] == values[7][2]:
        print("yah they match")
    else:
        print("nope")
        print(values[1][2])
        print(values[7][2])
    '''

    for i in range(3):
        print(i)
        check(swipe, values);
        c_val += 5
        rangeName = filename + '!' + startcol + str(a_val) + ':' + endcol + str(c_val)
        i += 1
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
        values = result.get('values', [])


    create_new(service, spreadsheetId, swipe, values); #temporary disable


'''
Check receives a spreadsheet data array called values,
it then requests a hidden user input called swipe; prompting user to swipe
the mag reader. It then loops through the values array, trying to match swipe to an
existing value
'''


def check(swipe, values):
    # swipe = getpass.getpass(prompt='Please swipe: ',stream=None)

    if len(swipe) != 25:  # length of GMU id strings
        # print(len(swipe)) #delete
        # print(swipe) #delete
        swipe_error(values)

    for row in values:
        try:
            if swipe == row[2]:
                print('Verified!')
                print('%s?' % row[0])
                exit();
        except IndexError:
            continue
            #print("Empty value ignored, continuing")

    return


def swipe_error(values):
    print('Uh-oh! Please swipe again:')
    check(values)


def create_new(service, spreadsheetId, swipe, values):
    print('You do not exist in our database!\nPlease follow the instructions for first time swipe-ins.')
    print(swipe)

    firstname = input('First name: ')
    lastname = input('Last name: ')

    # *********************
    # This write is a default test
    # range_ = 'ID!E1:G2' #E,F,G
    range_ = 'ID!A2:C7'  # A,B,C
    value_input_option = 'RAW'
    value_range_body = {"majorDimension": "rows", "values": [[firstname, lastname, swipe]]}

    '''This is the syntax for value range body
        value_range_body = {
      "majorDimension": "columns",
      "values": [
        [
          213,
          345
        ],
        [
          100,
          312
        ]
      ]
    }
    '''
    #Below is used to write (append) to the current data table (sheet) selected
    # request = service.spreadsheets().values().update(spreadsheetId=spreadsheetId,range=range_,valueInputOption=value_input_option,body=value_range_body)
    request = service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range=range_, valueInputOption=value_input_option, body=value_range_body)
    response = request.execute()
    pprint(response)  #print a response to the screen


if __name__ == '__main__':
    main()
