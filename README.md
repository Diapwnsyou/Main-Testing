# Main-Testing
[![Build Status](https://travis-ci.org/Diapwnsyou/Main-Testing.svg?branch=master)](https://travis-ci.org/Diapwnsyou/Main-Testing)

This is just a simple script that hits open movie database with an API call for whatever movie or show you want to search. It will return a formatted result:

## movie.py --movie iron man
```
Title: Iron Man
Ratings:
	Internet Movie Database: 7.9/10
	Rotten Tomatoes: 94%
	Metacritic: 79/100
Genre: Action, Adventure, Sci-Fi
Plot:
  After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.
Starring:
  Robert Downey Jr., Terrence Howard, Jeff Bridges, Gwyneth Paltrow
```

Or as a json string without elminating or formatting any data.

## movie.py --movie iron man --json
```
{u'Plot': u'After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.', u'Rated': u'PG-13', u'Title': u'Iron Man', u'Ratings': [{u'Source': u'Internet Movie Database', u'Value': u'7.9/10'}, {u'Source': u'Rotten Tomatoes', u'Value': u'94%'}, {u'Source': u'Metacritic', u'Value': u'79/100'}], u'DVD': u'30 Sep 2008', u'Writer': u'Mark Fergus (screenplay), Hawk Ostby (screenplay), Art Marcum (screenplay), Matt Holloway (screenplay), Stan Lee (characters), Don Heck (characters), Larry Lieber (characters), Jack Kirby (characters)', u'Production': u'Paramount Pictures', u'Actors': u'Robert Downey Jr., Terrence Howard, Jeff Bridges, Gwyneth Paltrow', u'Type': u'movie', u'imdbVotes': u'772,926', u'Website': u'http://www.ironmanmovie.com/', u'Poster': u'https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX300.jpg', u'Director': u'Jon Favreau', u'Released': u'02 May 2008', u'Awards': u'Nominated for 2 Oscars. Another 20 wins & 65 nominations.', u'Genre': u'Action, Adventure, Sci-Fi', u'imdbRating': u'7.9', u'Language': u'English, Persian, Urdu, Arabic, Hungarian', u'Country': u'USA', u'BoxOffice': u'$318,298,180', u'Runtime': u'126 min', u'imdbID': u'tt0371746', u'Metascore': u'79', u'Response': u'True', u'Year': u'2008'}
```
