from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


# A class which allows for accessing and manipulating a google sheet
class SheetMutator:

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Sheets API Python Quickstart'

    # Posts the provided timestamp value to the google sheet
    def post_timestamp(self, value):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

        spreadsheetId = '1NyZkpeOIuEILLWfRbmpsLv4lCP-O5wJzpqPvTHkSCb4'
        rangeName = 'Sheet1!A:A'
        valueInputOption = "USER_ENTERED"

        list = [[value]]
        resource = {
            "majorDimension": "ROWS",
            "values": list
        }

        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheetId,
            range=rangeName,
            body=resource,
            valueInputOption=valueInputOption).execute()

    # Grabs the latest timestamp from the google sheet
    def get_previous_timestamp(self):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

        spreadsheetId = '1NyZkpeOIuEILLWfRbmpsLv4lCP-O5wJzpqPvTHkSCb4'
        rangeName = 'Sheet1!A:A'

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range=rangeName).execute()

        values = result.get('values', [])

        if not values:
            return "This is your first time logging in!"
        else:
            return "".join(values[-1])

    # Acquired credentials necessary for accessing the google sheet
    def get_credentials(self):
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
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials