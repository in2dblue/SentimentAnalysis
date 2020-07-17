import nltk
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents

#print(nltk.__version__)
#print(twitter_samples.fileids())

#Each tweet is represented as one string
#tweets = twitter_samples.strings('positive_tweets.json')

# Load tokenized tweets
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')
#Tag tokenized tweets
tweets_tagged = pos_tag_sents(tweets_tokens)
#print(tweets_tagged)

JJ_count = 0 #Adjective
NN_count = 0 #Singular Noun; plural is NNS

for tweet in tweets_tagged:
    for pair in tweet:
        tag = pair[1]
        if tag == 'JJ':
            JJ_count += 1
        elif tag == 'NN':
            NN_count += 1

print('Total Adjectives: ', JJ_count)
print('Total Noun: ', NN_count)