from numpy import array
from keras.preprocessing.text import one_hot, Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers.embeddings import Embedding
from nltk.tokenize import word_tokenize

corpus = [
    # Positive Reviews

    'This is an excellent movie',
    'The move was fantastic I like it',
    'You should watch it is brilliant',
    'Exceptionally good',
    'Wonderfully directed and executed I like it',
    'Its a fantastic series',
    'Never watched such a brillent movie',
    'It is a Wonderful movie',

    # Negtive Reviews

    "horrible acting",
    'waste of money',
    'pathetic picture',
    'It was very boring',
    'I did not like the movie',
    'The movie was horrible',
    'I will not recommend',
    'The acting is pathetic'
]

sentiments = array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])

# Method1: one_hot to convert text to vectors
# all_words = []
# for sent in corpus:
#     tokenize_word = word_tokenize(sent)
#     for word in tokenize_word:
#         all_words.append(word)
#
# unique_words = set(all_words)
# vocab_length = 50
#
# embedded_sentences = [one_hot(sent, vocab_length) for sent in corpus]

# Method2: Tokenizer to convert text to vectors
word_tokenizer = Tokenizer()
word_tokenizer.fit_on_texts(corpus)
vocab_length = len(word_tokenizer.word_index) + 1  # Added 1 to store the dimensions for the words for which no pretrained word embeddings exist
embedded_sentences = word_tokenizer.texts_to_sequences(corpus)
print(embedded_sentences)

word_count = lambda sentence: len(word_tokenize(sentence))
longest_sentence = max(corpus, key=word_count)
length_longest_sentence = len(word_tokenize(longest_sentence))

padded_sentences = pad_sequences(embedded_sentences, length_longest_sentence, padding='post')
print(padded_sentences)

# Model
model = Sequential()
model.add(Embedding(vocab_length, 20, input_length=length_longest_sentence))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
print((model.summary()))

model.fit(padded_sentences, sentiments, epochs=100, verbose=1)
loss, accuracy = model.evaluate(padded_sentences, sentiments, verbose=0)
print('Accuracy: %f' % (accuracy*100))