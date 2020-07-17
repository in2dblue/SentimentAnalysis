from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence

#positive_tweets = twitter_samples.strings('positive_tweets.json')
#negative_tweets = twitter_samples.strings('negative_tweets.json')
#text = twitter_samples.strings('tweets.20150430-223406.json')

# tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
# print(tweet_tokens)
# print(lemmatize_sentence(tweet_tokens[0]))
abc = {}
a={}
abc[a['ankit']] = 5
print(abc)