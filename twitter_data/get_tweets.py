import tweepy
import pprint
import config
import pandas as pd

import re

auth = tweepy.OAuthHandler(config.CREDENTIALS['consumer']['key'], config.CREDENTIALS['consumer']['secret'])
auth.set_access_token(config.CREDENTIALS['access']['token'], config.CREDENTIALS['access']['secret'])
api = tweepy.API(auth)


full_tweets = []
short_tweet_sentences = []
long_tweet_sentences = []

#setting character length
short_sentence_threshold = 55
long_sentence_threshold = 175

def preprocess(tweets):
    for tweet in tweets:
        tweet_text = tweet._json['full_text']

        filtered_tweet_text = re.sub(r'http\S+', '', tweet_text.replace('\n', ''))
        full_tweets.append(filtered_tweet_text)

        #assuming sentence ends with '. '
        tweet_sentences = filtered_tweet_text.split('. ')
        for sentence in tweet_sentences:
            if sentence != '':
                len_sents = len(sentence)
                if len_sents < short_sentence_threshold:
                    short_tweet_sentences.append(sentence)
                elif len_sents > short_sentence_threshold and len_sents < long_sentence_threshold:
                    long_tweet_sentences.append(sentence)


def write_data_to_file(filename, data_set):
    with open(filename, 'w') as f:
        for i, data_part in enumerate(data_set):
            f.write('%i. %s.\n' % (i+1, str(data_part)))



user = api.get_user('BarackObama')
obama_data = api.user_timeline(id='BarackObama', count=20, tweet_mode='extended')
preprocess(obama_data)

write_data_to_file('full_tweets.txt', full_tweets)
write_data_to_file('short_tweet_sentences.txt', short_tweet_sentences)
write_data_to_file('long_tweet_sentences.txt', long_tweet_sentences)
