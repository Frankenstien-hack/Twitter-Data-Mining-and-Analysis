import sys
import json
import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
	
	text = text.lower()   #turn the text in lower case
	tokens = tokenizer.tokenize(text)   #tokenising the text
	return [tk for tk in tokens if tk not in stopwords and not tk.isdigit()]

if __name__ == '__main__':
    
	filename = sys.argv[1]
	tweet_tokenizer = TweetTokenizer()
	punctuation = list(string.punctuation)
	stopword_list = stopwords.words('english') + punctuation + ['rt', 'via', '...']

	tf = Counter()
	with open("json/"+filename, 'r') as f:
		for line in f:
			tweet = json.loads(line)
			tokens = process(text=tweet['text'], tokenizer=tweet_tokenizer, stopwords=stopword_list)
			tf.update(tokens)
		for tag, count in tf.most_common(30):
			print("{}: {}".format(tag, count))
	
#for graph
	y = [count for tag, count in tf.most_common(30)]
	x = range(1, len(y)+1)
	plt.bar(x, y)
	plt.title("Term Frequencies")
	plt.ylabel("Frequency")
	plt.savefig('term_distribution.png')

