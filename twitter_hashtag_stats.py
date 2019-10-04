import sys
import json
from collections import defaultdict

def gethashtags(tweet):
    
	entities = tweet.get('entities', {})
	hashtags = entities.get('hashtags', [])
	return [tag['text'].lower() for tag in hashtags]

def usage():
    
	print("Usage:")
	print("python {} <filename.jsonl>".format(sys.argv[0]))

if __name__ == '__main__':
    
	if len(sys.argv) != 2:
		usage()
		sys.exit(1)
  
	filename = sys.argv[1]
 
	with open("json/"+filename, 'r') as f:

		hashtagcount = defaultdict(int)
		for line in f:
			tweet = json.loads(line)
			hashtagsintweet = gethashtags(tweet)
			numberofhashtags = len(hashtagsintweet)
			hashtagcount[numberofhashtags] += 1
   
		tweetswithhashtags = sum([count for numberoftags, count in hashtagcount.items() if numberoftags > 0])
		tweetswithnohashtags = hashtagcount[0]
		totaltweets = tweetswithnohashtags + tweetswithhashtags
		tweetswithhashtagspercent = "%.2f" % (tweetswithhashtags / totaltweets * 100)
		tweetswithnohashtagspercent = "%.2f" % (tweetswithnohashtags / totaltweets * 100)

		print("{} tweets without hashtags ({}%)".format(tweetswithnohashtags, tweetswithnohashtagspercent))
		print("{} tweets with at least one hashtag ({}%)".format(tweetswithhashtags, tweetswithhashtagspercent))

		for tagcount, tweetcount in hashtagcount.items():
			if tagcount > 0:
				percenttotal = "%.2f" % (tweetcount / totaltweets * 100)
				percentelite = "%.2f" % (tweetcount / tweetswithhashtags * 100)
				print("{} tweets with {} hashtags ({}% total, {}% elite)".format(tweetcount, tagcount, percenttotal, percentelite))
