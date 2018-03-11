#!/usr/bin/env python
'''Script that searches open movie database for movies or shows.
Output can be formatted or sent entirely as a json string.'''

import argparse
import sys
import json
import requests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('''A script that calls openmoviedb
                                                  to get movie information. Return
                                                  data can be formatted text or json.'''))
    parser.add_argument('--m', '--movie', dest='movie',
                        nargs='+', help='Provide Movie or show title to search for')
    parser.add_argument('--json', action='store_true',
                        help='Keeps API response in json format')

    args = parser.parse_args()
    api_key = ''

    try:
        with open('movie_api_key', 'r') as fh_key:
            api_key = fh_key.read().strip()
    except IOError:
        sys.exit('Exiting:\n  API key file not found!')

    if args.movie:
        movie = "+".join(args.movie)
        req_url = 'http://www.omdbapi.com/?t={}&apikey={}'.format(movie, api_key)
        try:
            response = requests.get(req_url)
            if response.status_code != 200:
                sys.exit('Exiting:\n  API error code {}'.format(response.status_code))
            data = json.loads(response.text)

            if not args.json:
                print 'Title: {}'.format(data['Title'])
                print 'Ratings:'
                for source in data['Ratings']:
                    print '\t{}: {}'.format(source['Source'], source['Value'])
                print 'Genre: {}'.format(data['Genre'])
                print 'Plot:\n  {}'.format(data['Plot'])
                print 'Starring:\n  {}'.format(data['Actors'])
            else:
                print data
        except KeyError:
            sys.exit('Exiting:\n  Error finding movie or show')
    else:
        parser.print_help()
        sys.exit(1)
