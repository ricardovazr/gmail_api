from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import base64
from email.message import EmailMessage

import random
import names

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.settings.basic']

class api():
    def __ini__(self):
        None
    

    def __auth(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        path = './'
        credential_file = path + 'credentials.json'
        token_file = path + 'token.json'

        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credential_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_file, 'w') as token:
                token.write(creds.to_json())
        return creds

    def __mymail(self):
            creds = self.__auth()
            
            try:
                # Call the Gmail API
                service = build('gmail', 'v1', credentials=creds)
                results = service.users().getProfile(userId='me').execute()
                return results['emailAddress']

            except HttpError as error:
                # TODO(developer) - Handle errors from gmail API.
                print(f'An error occurred: {error}')


    def gmail_send_message(self, param=0):
        creds = self.__auth()
        my_email = self.__mymail()
        #

        try:
            service = build('gmail', 'v1', credentials=creds)
            message = EmailMessage()

            message.set_content(param['body'])

            message['To'] = param['to']
            message['From'] = param['from']
            message['Subject'] = param['subject']


            # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            create_message = {
                'raw': encoded_message
            }
            
            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            print(F'Message Id: {send_message["id"]}')
        except HttpError as error:
            print(F'An error occurred: {error}')

            print('TIP!')
            print('This function requires a list of params as below')
            print("""param = {'from': email_from,
                     'to': email_to,
                     'subject': text_subject,
                     'body': text_body}""")
            send_message = None
        return send_message

    
    def generate_sample(self, num_sample=10):
        my_email = self.__mymail()

        for i in range(num_sample):
            job_role = random.choice(['Data engineer', 'Data analyst', 'Data scientist', 'BI analyst', 'Product Owner', 'Product Manager', 'Tech Lead'])
            
            candidate_name = names.get_full_name()#f"candidate {random.randrange(1000,9999)}"
            mail_prefix = candidate_name.lower().replace(' ', '_')
            param = {'from': mail_prefix + '@mail.com',
            'to': my_email,
            'subject': f"SampleCV - {job_role}",
            'body': f"Hi, I would like to apply for the {job_role} position.\n\nKind regards.\n{candidate_name}"}
            
            self.gmail_send_message(param)

        
    def gmail_search_message(self, word_search=''):
        creds = self.__auth()
        if word_search == '':
            print('Please write the word parameter you are looking for')
        try:
            service = build('gmail', 'v1', credentials=creds)

            search_message = (service.users().messages().list
                            (userId="me", q=word_search).execute())
            
            print(search_message)
           
        except HttpError as error:
            print(F'An error occurred: {error}')
          
        return search_message
    

    def read_message(self,id_message=0):
        creds = self.__auth()
        try:
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().get(userId='me', id=id_message, format='full').execute()
            return results

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')

    def welcome(self):
        return self.__mymail()
        
#if __name__ == '__main__':
try:

    welcome_message = api().welcome()

    if welcome_message.count('@') > 0:
        print(f"Welcome {welcome_message}.\nThe gmail API is ready to use.")
except Exception as e:
    print('API is not ready to use. \n Please revise your credentials or contact the admin.')
