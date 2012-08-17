import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run
CLIENT_SECRETS = '/Users/adamhammouda/CodeProjects/heroku-PersonalPage/repo/src/home_page/ganalytics_sandbox/client_secrets.json'
MISSING_CLIENT_SECRETS_MESSAGE = '%s is missing' % CLIENT_SECRETS
FLOW = flow_from_clientsecrets(CLIENT_SECRETS,scope='https://www.googleapis.com/auth/analytics.readonly',message=MISSING_CLIENT_SECRETS_MESSAGE)
