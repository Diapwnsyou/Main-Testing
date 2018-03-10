#!/usr/bin/env python

import argparse
import sys
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A script that calls openmoviedb to get movie information. Data return can be normal text or json.")
    parser.add_argument('--m', '--movie', dest='movie', nargs='+', help="Provide Movie title to search for")    

    args = parser.parse_args()
    api_key = ''

    with open('movie_api_key', 'r') as fh_key:
        api_key = fh_key.read().strip()

    if args.movie:
        movie = "+".join(args.movie)
        req_url = 'http://www.omdbapi.com/?t={movie}&apikey={key}'.format(movie=movie, key=api_key)
        print req_url
    else:
        parser.print_help()
        sys.exit(1)

