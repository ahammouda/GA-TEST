import sys
# import the Auth Helper class
import hello_analytics_api_v3_auth

from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError

def main(argv):
    # Initialize the Analytics Service Object
    analytics_service_object = hello_analytics_api_v3_auth.initialize_service()
    
    WEB_PROPERTY_ID = hello_analytics_api_v3_auth.WEB_PROPERTY_ID
    
    try:
        profiles_response = analytics_service_object.management().profiles().list(  #Note that you needed to edit this to profiles_response from the docs
            accountId=WEB_PROPERTY_ID.split('-')[1],
            webPropertyId=WEB_PROPERTY_ID).execute()
        
    except TypeError, error:
        # Handle errors in constructing a query.
        print ('There was an error in constructing your profiles query : %s' % error)
        
    except HttpError, error:
        # Handle API errors.
        print ('Arg, there was an API error with your profiles query : %s : %s' %
               (error.resp.status, error._get_reason()))
        
    profiles_response.get('items').index({'name'})
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

if __name__ == '__main__':
  main(sys.argv)
