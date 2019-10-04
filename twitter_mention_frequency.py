import sys
import json
from collections import Counter

def getmentions(tweet):
    
	entities = tweet.get('entities', {})
	mentions = entities.get('user_mentions', [])
	return [tag['screen_name'].lower() for tag in mentions]

if __name__ == '__main__':
    
	filename = sys.argv[1]
	with open("json/"+filename, 'r') as f:
		users = Counter()
		for line in f:
			tweet = json.loads(line)
			mentionsintweet = getmentions(tweet)
			users.update(mentionsintweet)
   
		for user, count in users.most_common(20):
			print("{}: {}".format(user, count))
