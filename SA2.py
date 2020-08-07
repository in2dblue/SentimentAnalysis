from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk import FreqDist, classify, NaiveBayesClassifier

import re, string, random, pickle, joblib
import _pickle as cPickle

# def lemmatize_sentence(tokens):
#     lemmatizer = WordNetLemmatizer()
#     lemmatized_sentence = []
#     for word, tag in pos_tag(tokens):
#         if tag.startswith('NN'):
#             pos = 'n'
#         elif tag.startswith('VB'):
#             pos = 'v'
#         else:
#             pos = 'a'
#         lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
#     return lemmatized_sentence

# positive_tweets = twitter_samples.strings('positive_tweets.json')
# negative_tweets = twitter_samples.strings('negative_tweets.json')
# text = twitter_samples.strings('tweets.20150430-223406.json')
# tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
# print(tweet_tokens)
# print(lemmatize_sentence(tweet_tokens[0]))
# print(remove_noise(tweet_tokens[0], stop_words))

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

# model requires not just a list of words in a tweet,
# but a Python dictionary with words as keys and True as values.
# convert the tweets from a list of cleaned tokens to dictionaries
# with keys as the tokens and True as values
def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

def create_model():
    stop_words = stopwords.words('english')

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    # print(positive_tweet_tokens)
    # print(positive_cleaned_tokens_list)

    #FINDING WORD DISTRIBUTION
    # all_pos_words = get_all_words(positive_cleaned_tokens_list)
    # freq_dist_pos = FreqDist(all_pos_words)
    # print(freq_dist_pos.most_common(10))

    # MODEL PREPARATION
    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)
    # code attaches a Positive or Negative label to each tweet
    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]
    # print(positive_dataset)
    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]
    dataset = positive_dataset + negative_dataset
    random.shuffle(dataset)
    # number of tweets is 10000 -- ratio of 70:30 for training and testing
    train_data = dataset[:7000]
    test_data = dataset[7000:]

    # MODEL TRAINING
    classifier = NaiveBayesClassifier.train(train_data)
    # MODEL SAVING WITH PICKLE
    filename = 'model/model_pickle1.sav'
    pickle.dump(classifier, open(filename, 'wb'))
    # MODEL SAVING WITH cPICKLE
    filename = 'model/model_cpickle1.sav'
    cPickle.dump(classifier, open(filename, 'wb'))
    # MODEL SAVING WITH JOBLIB
    filename = 'model/model_joblib1.sav'
    joblib.dump(classifier, filename)

    # MODEL ACCURACY
    print("Accuracy is:", classify.accuracy(classifier, test_data))
    print(classifier.show_most_informative_features(10))

if __name__ == "__main__":
    ########### create_model()
    # MODEL LOAD WITH PICKLE
    classifier = pickle.load(open('model/model_pickle1.sav', 'rb'))
    # MODEL LOAD WITH cPICKLE
    classifier1 = cPickle.load(open('model/model_pickle1.sav', 'rb'))
    # MODEL LOAD WITH JOBLIB
    classifier2 = joblib.load('model/model_joblib1.sav')

    # MODEL PERFORMANCE ON RANDOM TWEET  II Sarcasm, Positive then Negative in order
    # custom_tweet = 'Thank you for sending my baggage to CityX and flying me to CityY at the same time. Brilliant service. #thanksGenericAirline'
    # custom_tweet = 'Congrats #SportStar on your 7th best goal from last season winning goal of the year :) #Baller #Topbin #oneofmanyworldies'
    custom_tweet = "I ordered just once from TerribleCo, they screwed up, never used the app again."
    custom_tokens = remove_noise(word_tokenize(custom_tweet))
    print(classifier.classify(dict([token, True] for token in custom_tokens)))