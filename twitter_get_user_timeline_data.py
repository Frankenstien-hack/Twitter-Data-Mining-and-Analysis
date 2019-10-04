import sys
import json
from tweepy import Cursor
from twitter_client_auth import get_twitter_client

if __name__ == '__main__':

    user = sys.argv[1]
    client = get_twitter_client()

    #name = "{}_home_timeline.jsonl".format(user)

    with open("json/{}_home_timeline.jsonl".format(user), 'w') as f:
        for pages in Cursor(client.user_timeline, screen_name=user, count=200).pages(16): # max limit = 3200 for user timeline
            for status in pages:
                f.write(json.dumps(status._json)+"\n")
