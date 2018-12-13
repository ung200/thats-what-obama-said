import config
import os


## run twitter script
twitter_dir = config.DIRS['twitter']
#os.system('python %s' % twitter_dir+'get_tweets.py')
print('python %s' % twitter_dir+'get_tweets.py')


## get obama wav from his youtube address
obama_address_dir = config.DIRS['obama_address']
os.system('bash %sfetch.sh 8 11' % obama_address_dir)



