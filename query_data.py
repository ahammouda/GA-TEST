import sys

# import the Auth Helper class
import hello_analytics_api_v3_auth

from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError

def main(argv):
    # Initialize the Analytics Service Object
    analytics_service_object = hello_analytics_api_v3_auth.initialize_service()
    
    try:
        #List the accounts
        accounts_response = analytics_service_object.management().accounts().list().execute()
        

    except TypeError, error:
        # Handle errors in constructing a query.
        print ('There was an error in constructing your accounts query : %s' % error)
    
    except HttpError, error:
        # Handle API errors.
        print ('Arg, there was an API error with your accounts query: %s : %s' %
               (error.resp.status, error._get_reason()))
    
    
    for i in range(len(accounts_response.get('items'))):
        if accounts_response.get('items')[i]['name']=='Adam GH':
            account_id = accounts_response.get('items')[i].get('id')
            print 'Account ID      = %s' % accounts_response.get('items')[i].get('id')
            print 'Account Name    = %s' % accounts_response.get('items')[i].get('name')
            print 'Created         = %s' % accounts_response.get('items')[i].get('created')
            print 'Updated         = %s' % accounts_response.get('items')[i].get('updated')

    try:
        webproperties_response = analytics_service_object.management().webproperties().list(
            accountId=account_id).execute()
    
    except TypeError, error:
        # Handle errors in constructing a query.
        print ('There was an error in constructing your webproperties query : %s' % error)
    
    except HttpError, error:
        # Handle API errors.
        print ('Arg, there was an API error with your webproperties query : %s : %s' %
               (error.resp.status, error._get_reason()))
    
    for webproperty in webproperties_response.get('items', []):
            print '\t Account ID         = %s' % webproperty.get('accountId')
            print '\t Web Property ID    = %s' % webproperty.get('id')
            print '\t Web Property Name  = %s' % webproperty.get('name')
            print '\t Internal Web Property ID = %s' % webproperty.get('internalWebPropertyId')
            
            print '\t Website URL        = %s' % webproperty.get('websiteUrl')
            print '\t Created            = %s' % webproperty.get('created')
            print '\t Updated            = %s' % webproperty.get('updated')
    
            if webproperty.get('websiteUrl') == 'http://www.adamgh.com':
                webproperty_id = webproperty.get('id')
    
    try:
        profiles_response = analytics_service_object.management().profiles().list(  #Note that you needed to edit this to profiles_response from the docs
            accountId=account_id,
            webPropertyId=webproperty_id).execute()
        
    except TypeError, error:
        # Handle errors in constructing a query.
        print ('There was an error in constructing your profiles query : %s' % error)
        
    except HttpError, error:
        # Handle API errors.
        print ('Arg, there was an API error with your profiles query : %s : %s' %
               (error.resp.status, error._get_reason()))
        
        
    for profile in profiles_response.get('items', []):
        print '\t \t Account ID                = %s' % profile.get('accountId')
        print '\t \t Web Property ID           = %s' % profile.get('webPropertyId')
        print '\t \t Internal Web Property ID  = %s' % profile.get('internalWebPropertyId')
        print '\t \t Profile ID                = %s' % profile.get('id')
        print '\t \t Profile Name              = %s' % profile.get('name')
        
        print '\t \t Default Page                    = %s' % profile.get('defaultPage')
        print '\t \t Exclude Query Parameters        = %s' % profile.get('excludeQueryParameters')
        print '\t \t Site Search Category Parameters = %s' % profile.get('siteSearchCategoryParameters')
        print '\t \t Site Search Query Parameters    = %s' % profile.get('siteSearchQueryParameters')
        
        print '\t \t Currency = %s' % profile.get('currency')
        print '\t \t Timezone = %s' % profile.get('timezone')
        print '\t \t Created  = %s' % profile.get('created')
        print '\t \t Updated  = %s' % profile.get('updated')

def get_results(service, profile_id):
  # Use the Analytics Service Object to query the Core Reporting API
  return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date='2012-03-03',
      end_date='2012-03-03',
      metrics='ga:visits').execute()


def print_results(results):
  # Print data nicely for the user.
  if results:
    print 'First Profile: %s' % results.get('profileInfo').get('profileName')
    print 'Total Visits: %s' % results.get('rows')[0][0]
  
  else:
    print 'No results found'


if __name__ == '__main__':
  main(sys.argv)
