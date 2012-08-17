import sys, string
from operator import itemgetter
# import the Auth Helper class
import hello_analytics_api_v3_auth

from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError

NUM_FIELDS = 4

def main(argv):
    # Initialize the Analytics Service Object
    analytics_service_object = hello_analytics_api_v3_auth.initialize_service()
    
    results = get_results(analytics_service_object, hello_analytics_api_v3_auth.PROFILE_ID)
    
    sort_results(results, NUM_FIELDS)
    #print_results(results)


def get_results(service, profile_id):
  # Use the Analytics Service Object to query the Core Reporting API
  return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date='2012-07-30',                         #This is the entire time I've been live
      end_date='2012-08-16',
      metrics='ga:bounces,ga:timeOnSite',
      dimensions='ga:visitLength,ga:visitCount').execute()

def sort_results(results, num_fields):
    '''
    dimensions      metrics
    ============   ============
    visitLength     bounces
    visitCount      timeOnSite
    '''
    
    #sort rows by visit length
    #print results
    for i in range(len( results.get('rows'))):
        print results.get('rows')[i]
    
    #print results.get('rows')[0][:]
    #print results.get('rows')[:][0]
    #print results.get('rows')[2][3]
    
    print '\n'
    results_ints = []
    for i in range(len(results.get('rows'))):
        row = []
        for j in range(num_fields):
            try:
                row.append(int(results.get('rows')[i][j]))
            except ValueError:
                row.append(float(results.get('rows')[i][j]))
        
        results_ints.append(row)
        print results_ints[i]
    
    results_n = sorted(results_ints, key=itemgetter(0) ) ######### This needs some genericification
    
    print '\n'
    for i in range(len(results_n)):
        print results_n[i]
        

def print_results(results):
    # Print data nicely for the user.
  
    # Print headers.
    output = []
    for header in results.get('columnHeaders'):
        output.append('%30s' % header.get('name'))
        print ''.join(output)
    
    # Print rows.
    if results.get('rows', []):
        for row in results.get('rows'):
            output = []
            for cell in row:
                output.append('%30s' % cell)
                print ''.join(output)
    else:
        print 'No results found'
    
    query = results.get('query')
    for key, value in query.iteritems():
        print '%s = %s' % (key, value)
    

if __name__ == '__main__':
  main(sys.argv)
