import sys
import json
from collections import Counter

def gethashtags(tweet):
    
	entities = tweet.get('entities', {})
	hashtags = entities.get('hashtags', [])
	return [tag['text'].lower() for tag in hashtags]

if __name__ == '__main__':
    
	filename = sys.argv[1]
	with open("json/"+filename, 'r') as f:
		hashtags = Counter()
		for line in f:
			tweet = json.loads(line)
			hashtagsintweet = gethashtags(tweet)
			hashtags.update(hashtagsintweet)
   
		for tag, count in hashtags.most_common(20):
			print("{}: {}".format(tag, count))
