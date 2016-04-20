# -*- coding: utf-8 -*-
from twython import TwythonStreamer
from twython import Twython
import sys
import pdb
from unidecode import unidecode
from datetime import datetime, timedelta
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import vincent

print(sys.version)
# Example obtained from http://aylien.com/super-bowl-50-tweets
# Authentication keys
token = "720636802625859584-3UrFzmlVHpVKx4sa5WUMHUWLTgbEdeP"
tsecret = "2VMKPgVVMNswAxpCBUQhZM5A8GczFNoJc8FbuAsnKX6qf"
key = "UR3PGjNAJi69QYQw7wm1BppsZ"
ksecret= "Zoer8754SIzZcljncsnvR0XLy3NGBvH87LfO0bIzSv8j6PUgea"

# # Authenticate and create a Twitter handle
# twitter = Twython(key, ksecret, token, tsecret)
# print("Authentication")

# # Set the search keywords
# query = "Broncos -RT"

# # Set the language (optional)
# lang = "en"

# # Set the maximum number of tweets that should be retrieved (optional/max = 100) 
# count = 5

# result = twitter.search(q=query, lang=lang, count=count)
# print("Recherche")

# # Query result information
# search_info = result['search_metadata']
# print("Résultats")

# print("Query time: {}".format(search_info['completed_in']))
# print("Number or tweets retrieved: {}".format(search_info['count']))


if __name__ == "__main__":
	# Second method : Based on Alyen example
	# 1 - Connexion to Twitter API, make query with a number of maximum tweets, and tags
	client_args = {
	    'proxies': {
	        'http': 'http://empweb1.ey.net:8080/',
	        'https': 'http://empweb1.ey.net:8443/',
	    }
	}

	twitter = Twython(key, ksecret, token, tsecret, client_args = client_args)	
	teamName1 = "France"
	teamName2 = "Italie"
	queryList = [teamName1, teamName2]
	resultByTeams = []
	tweetsListByTeam = []
	lang = "fr"
	count = 5
	queryStartDatetime = datetime.now()
	for query in queryList:
		resultByTeam = twitter.search(q=query, lang=lang, count=count)
		resultByTeams.append(resultByTeam)
		# Query result information
		tweetsByTeam = resultByTeam['statuses']
		tweetsList = []
		for t in tweetsByTeam:	tweetsList.append(unidecode(t["text"]))
		tweetsListByTeam.append(tweetsList)

	timeToAdd = resultByTeam['search_metadata']['completed_in']
	timeQueryInterval = [queryStartDatetime, queryStartDatetime + timedelta(timeToAdd)]
	
	# 2 - Preprocessing 
	#


	# 3 - Gather data and build interesing features for display 
	volumeTweets = {}
	volumeTweets[teamName1] = len(tweetsListByTeam[0])
	volumeTweets[teamName2] = len(tweetsListByTeam[1])

	# 3.1 Sentiment analysis : polarity (subjectivity is available also)
	testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
	testimonial.sentiment.polarity
	text = "Tout va très bien"
	analyseTexteFr = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
	# 4 - Display
	data = {'data': [10, 20, 30], 'x': ["Positive", "Negative", "Positive"]}
	bar = vincent.Bar(data, iter_idx='x')
	bar.to_json('term_freq.json', html_out=True, html_path='chart.html')