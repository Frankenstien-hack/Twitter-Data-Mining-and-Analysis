import sys
import json
import numpy as np

def usage():
	print("Usage:")
	print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    
	if len(sys.argv) != 2:
		usage()
		sys.exit(1)
  
	screenname = sys.argv[1]
	fileoffollowers = 'users/{}/followers.jsonl'.format(screenname)
	fileoffriends = 'users/{}/friends.jsonl'.format(screenname)
 
	with open(fileoffollowers) as f1, open(fileoffriends) as f2:
	
		followers = []
		friends = []
		for line in f1:
			profile = json.loads(line)
			followers.append(profile['screen_name'])
		for line in f2:
			profile = json.loads(line)
			friends.append(profile['screen_name'])
   
		followers = np.array(followers)
		friends = np.array(friends)
		
		mutualfriends = np.intersect1d(friends, followers, assume_unique=True) 
		followersnotfollowing = np.setdiff1d(followers, friends, assume_unique=True)
		friendsnotfollowing = np.setdiff1d(friends, followers, assume_unique=True)
		
		print("{} has {} followers".format(screenname, len(followers)))
		print("{} has {} friends".format(screenname, len(friends)))
		print("{} has {} mutual friends".format(screenname, len(mutualfriends)))
		print("{} friends are not following {} back".format(len(friendsnotfollowing), screenname))
		print("{} followers are not followed back by {}".format(len(followersnotfollowing), screenname))