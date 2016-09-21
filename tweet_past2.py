# -*- coding: utf-8 -*-

import re, tweepy, time

from api_keys import *

url = 'https://api.twitter.com/1.1/statuses/update.json'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def preparing_text_file(file_name):
	# tweet_separator = " [...]"
	with open(file_name, 'r') as my_file:
		output = my_file.read()
		lines = output.split('\n')
    	regex = re.compile(r'.{1,134}(?:\s+|$)')
    	return '\n'.join(s.rstrip() for line in lines for s in regex.findall(line))


def writing_to_file(pieces):
	with open("tweet_archive.txt", 'w') as my_file:
		my_file.write(str(pieces))

def posting_to_twitter(tweets):
	with open("tweet_archive.txt", 'r+') as my_file:
		tweet_file = my_file.readlines()
	for line in tweet_file:
		line = line.strip(r'\n')
		if tweet_file[len(tweet_file)] != line:
			line = line + " [...]"
			api.update_status(status = line)
		with open ('tweet_archive.txt', 'w') as tweetfile:
			tweet_file.remove(line)
			tweetfile.writelines(tweet_file)
		time.sleep(300)

def main():
	prep = preparing_text_file("tweet_archive.txt")
	write = writing_to_file(prep)
	posting_to_twitter(write)

if __name__ == '__main__':
	main()
