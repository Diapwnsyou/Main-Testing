#!/usr/bin/env python

import argparse
import sys
import requests
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=("""A script that calls openmoviedb to get movie information.
                                                   Data return can be normal text or json."""))
    parser.add_argument('--m', '--movie', dest='movie',
                        nargs='+', help='Provide Movie title to search for')    
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
        req_url = 'http://www.omdbapi.com/?t={movie}&apikey={key}'.format(movie=movie, key=api_key)
        response = requests.get(req_url)
        if response.status_code != 200:
            sys.exit('Exiting:\n  API error code {}'.format(response.status_code))
        print response.status_code
        data = json.loads(response.text)
    else:
        parser.print_help()
        sys.exit(1)

    if not args.json:
        print 'Title: {}'.format(data['Title'])
        print 'Ratings:'
        for source in data['Ratings']:
            print '\t{} {}'.format(source['Source'],source['Value'])
        print 'Genre: {}'.format(data['Genre'])
        print 'Plot:\n\t{}'.format(data['Plot'])
    else:
        print data
