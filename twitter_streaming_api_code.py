import sys
import time
import string
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_client_auth import get_twitter_authentication

class CustomListener(StreamListener):

	def __init__(self, filename):    #Saving the tweets in file named on the given arguments
     
		filename = format_filename(filename)
		self.outfile = "stream_%s.jsonl" % filename

	def on_data(self, data):	    #called up when data is incoming
     								
		try:
			with open("json/"+self.outfile, 'a') as f:    #writting the streamed data in a file
				f.write(data)
				return True
		except BaseException as e:
			sys.stderr.write("Error on_data: {}\n".format(e))    
			time.sleep(5)    #To prevent an occassional network hiccup
		return True

	def on_error(self, status):    #called up when their is a 420 error
     
		if status == 420:
			sys.stderr.write("Rate limit exceeded\n")
			return False
		else:
			sys.stderr.write("Error: {}\n".format(status))
			return True

def format_filename(filename):

		return ''.join(convert_valid(eachchar) for eachchar in filename)

def convert_valid(eachchar):    # Convert a character into '_' if "invalid".
	
	validchars = "-_.%s%s" % (string.ascii_letters, string.digits)
	if eachchar in validchars:
		return eachchar
	else:
		return '_'

if __name__ == '__main__':
	
    query = sys.argv[1:]    # list of CLI arguments
    query_filename = ' '.join(query) 
    auth = get_twitter_authentication()
    twitter_stream = Stream(auth, CustomListener(query_filename))
    twitter_stream.filter(track=query, is_async=True)
