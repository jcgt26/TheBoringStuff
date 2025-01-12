import base64
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError, Error

import random

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_body(payload):
    if payload is None:
        raise Error('No payload found.')
    parts = payload.get('parts')
    body = None

    if parts is not None:
        for part in parts:
            if part.get('mimeType') == 'text/plain':
               body_from_part = part.get('body')
               data = body_from_part.get('data')
               if data is not None:
                   body = base64.urlsafe_b64decode(data).decode('utf-8')
    elif payload.get('body') is not None:
        body_from_simple_part = payload.get('body')
        data = body_from_simple_part.get('data')
        if data is not None:
            body = base64.urlsafe_b64decode(data).decode('utf-8')

    return body


class GmailClient:
  def __init__(self, credentials_file_name: str):
    self.credentialsFileName = credentials_file_name
    self.service = self.init_service()

  def init_service(self):
      """Shows basic usage of the Gmail API.
      Lists the user's Gmail labels.
      """
      creds = None
      # The file token.json stores the user's access and refresh tokens, and is
      # created automatically when the authorization flow completes for the first
      # time.
      if os.path.exists("token.json"):
          creds = Credentials.from_authorized_user_file("token.json", SCOPES)
      # If there are no (valid) credentials available, let the user log in.
      if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
              # There is an issue when the credential are expired,
              # for now the solution is to delete the token to force the auth process. maybe the refresh token is the issue?
              creds.refresh(Request())
          else:
              flow = InstalledAppFlow.from_client_secrets_file(
                  self.credentialsFileName, SCOPES
              )
              creds = flow.run_local_server(port=0)
          # Save the credentials for the next run
          with open("token.json", "w") as token:
              token.write(creds.to_json())

      try:
          # Call the Gmail API
          return build("gmail", "v1", credentials=creds)
          # results = service.users().labels().list().execute()
          # labels = results.get("labels", [])
          print('Service was initialized')
      #  printLabels(labels)
      except HttpError as error:
          print(f'An error occurred: {error}')

  def print_labels(self):
      self.validate_service()
      try:
          result = self.service.users().labels().list(
              userId='me',
          ).execute()
          if result.get('labels') is None:
              raise Error('No labels found.')

          with open('labels.txt', 'w') as file:
              for label in result['labels']:
                  file.write(label['name'] + '\n')

      except HttpError as error:
          print(f'Error while trying to fetch the labels: {error}')

  def get_messages_ref_by_limit(self, number_of_messages: int):
      self.validate_service()
      try:
          return self.service.users().messages().list(
              userId="me",
              maxResults=number_of_messages,  # Number of messages you want
              labelIds=['INBOX'],
          ).execute()

      except HttpError as error:
          print(f'Error occurred: {error}')
          return []

  """ 
  The message can have a simple part -> in which case we can check the body directly in the payload.
  The message can have multiple parts -> in which case we would have to iterate through each part.
  """
  def get_message_details(self, message_id):
      self.validate_service()
      try:
          message = self.service.users().messages().get(
              userId='me',
              id=message_id
          ).execute()
          payload = message.get('payload')
          print(message.get('payload'))
          if payload is None:
              raise Error('No payload found.')
          body = get_body(payload)
          if body is None:
              return {}
          return {
               'id': message_id,
               'body': body,
           }


      except HttpError as error:
          print(f'Error occurred, could not fetch the message: {error}')

  def validate_service(self):
      if self.service is None:
          raise HttpError('No service found.')
    






