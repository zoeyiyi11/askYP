#bot.py

import os
import tweepy, time, sys
from secrets import * 
from nltk.tag import pos_tag
import string
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import urllib



class StreamListener(tweepy.StreamListener):
	print "yo"
	def on_status(self, status):
		print "hey"
		try: 
			print "Hello World2"
			data = {}
			location = ""
			exclude = set('!?.,')

			location = status.place

			#with open('questions.json', 'a') as f: 
				
			print status.text
			print status.id
			print status.user.screen_name

			time.sleep(5)

			sentence = status.text.replace('#askYP', '')
			sentence = ''.join(ch for ch in sentence if ch not in exclude)
			tagged_sent = pos_tag(sentence.split())

			targets = [word for word, pos in tagged_sent if pos == 'NN' or pos == 'NNP']
	

			reponse = []
			collection = []
			try:
				for i in targets:
					url = 'http://hackaton.ypcloud.io/search?what=%s&longtitude=-73.516388&latitue=45.522554' % i
					response.append(urllib.urlopen(url))
			except BaseException as e:
				print "ERROR"
				exit(1)

			for j in response:
				collection.append(json.loads(response[j].read()))
			#with open('questions.json', 'r') as r:
			#	json_decode = json.load(r)
			
			stores = []
			location = []

			for info in collection:
				stores += info["merchants"]["businessName"]
				location +=info["address"]["displayLine"]
			

			api.update_status('@%s you want %s. You can find it at %s at %s' % (status.user.screen_name, targets[0], stores[0], location[0]), status.id)
			time.sleep(2)
			#api.update_status('next one yo')
			return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print status
		return True


if __name__ == '__main__':
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
	api = tweepy.API(auth)
	MyStreamListener = StreamListener()
	twitter_stream = Stream(auth, MyStreamListener)
	twitter_stream.filter(track=['#askYP'])