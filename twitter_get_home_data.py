import json
from tweepy import Cursor
from twitter_client_auth import get_twitter_client

if __name__ == '__main__':
	client = get_twitter_client()

	with open('json/client_home_timeline.jsonl', 'w') as f:
		for pages in Cursor(client.home_timeline, count=200).pages(4):  #max limit allowed by twitter api is 800
			for status in pages:
				f.write(json.dumps(status._json)+"\n")
