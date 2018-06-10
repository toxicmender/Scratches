#!/usr/bin/env python3

import shodan
import sys

SHODAN_API_KEY = "insert your API key here"
api = shodan.Shodan(SHODAN_API_KEY)

def search(query):
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search(query)

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    except shodan.APIError, e:
        print('Error: {}'.format(e))


def host(ip):
   # Lookup the host
   host = api.host(ip) # example ip = '217.140.75.46'

   # Print general info
    print("""
            IP: {}
            Organization: {}
            Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    # Print all banners
    for item in host['data']:
        print("""
                Port: {}
                Banner: {}
        """.format(item['port'], item['data']))

def iplookup():
    # Input validation
    if len(sys.argv) == 1:
        print("Usage: {} <search query>",format(sys.argv[0]))
        sys.exit(1)

    try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        query = ' '.join(sys.argv[1:])
        result = api.search(query)

        # Loop through the matches and print each IP
        for service in result['matches']:
                print service['ip_str']
    except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)
