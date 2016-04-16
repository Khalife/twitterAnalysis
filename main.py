from twython import Twython

# Example obtained from http://aylien.com/super-bowl-50-tweets
# Authentication keys
token = "720636802625859584-3UrFzmlVHpVKx4sa5WUMHUWLTgbEdeP"
tsecret = "2VMKPgVVMNswAxpCBUQhZM5A8GczFNoJc8FbuAsnKX6qf"
key = "UR3PGjNAJi69QYQw7wm1BppsZ"
ksecret= "Zoer8754SIzZcljncsnvR0XLy3NGBvH87LfO0bIzSv8j6PUgea"

# Authenticate and create a Twitter handle
twitter = Twython(key, ksecret, token, tsecret)
print("Authentication")

# Set the search keywords
query = "Broncos -RT"

# Set the language (optional)
lang = "en"

# Set the maximum number of tweets that should be retrieved (optional/max = 100) 
count = 5

result = twitter.search(q=query, lang=lang, count=count)
print("Recherche")

# Query result information
search_info = result['search_metadata']
print("Résultats")

print("Query time: {}".format(search_info['completed_in']))
print("Number or tweets retrieved: {}".format(search_info['count']))