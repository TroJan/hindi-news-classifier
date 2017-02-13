# -*- coding: utf-8 -*-

from collections import OrderedDict

from hinditokenizer import *


def preprocess_text_without_stemming(text):
    '''
        Receives a text(string). Returns a list

        Does the following action over it

        * Tokenizes the text
        * Removes hyphenated tokens(if present)
        * Removes stopwords
    '''
    tokens = tokenize(text)
    # remove hyphenated and duplicate hyphented words
    tokens = remove_hyphenated_tokens(tokens)
    stopwords = stopwords_list()

    no_stopwords_tokens = [token for token in tokens
                           if token.encode('utf8') not in stopwords]

    return no_stopwords_tokens


def create_bag_of_words(tokens):
    '''
        Create bag of words (freq dict) for given set of tokens
            {'word': count}

        Assumes that the tokens received is an array which has been
        preprocessed.

        Preprocessing here means that the tokens does not contain any
        stopwords.
    '''
    freq_map = OrderedDict()
    for token in tokens:
        # TODO: decide if stemming is required or not.
        stem_word = stem(token)
        freq_map.setdefault(stem_word, 0)
        freq_map[stem_word] += 1

    return freq_map
