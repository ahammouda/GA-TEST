#! /Users/adamhammouda/CodeProjects/GA-DJANGO-DEV/development/bin/python

import httplib2

from apiclient.discovery import build

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

CLIENT_SECRETS = '/Users/adamhammouda/CodeProjects/GA-DJANGO-DEV/development/gatestapp/GA-TEST/client_secrets.json'
MISSING_CLIENT_SECRETS_MESSAGE = '%s is missing' % CLIENT_SECRETS

FLOW = flow_from_clientsecrets(CLIENT_SECRETS,
  scope='https://www.googleapis.com/auth/analytics.readonly',
  message=MISSING_CLIENT_SECRETS_MESSAGE)

TOKEN_FILE_NAME = '/Users/adamhammouda/CodeProjects/GA-DJANGO-DEV/development/gatestapp/GA-TEST/analytics.dat'

WEB_PROPERTY_ID = 'UA-33670488-1'

PROFILE_ID = '62446682'

def get_account_id():
  return WEB_PROPERTY_ID.split('-')[1]

def get_webproperty_id():
  return WEB_PROPERTY_ID

def prepare_credentials():
  storage = Storage(TOKEN_FILE_NAME)
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    credentials = run(FLOW, storage)
  return credentials

def initialize_service():
  http = httplib2.Http()

  #Get stored credentials or run the Auth Flow if none are found
  credentials = prepare_credentials()
  http = credentials.authorize(http)

  #Construct and return the authorized Analytics Service Object
  return build('analytics', 'v3', http=http)
