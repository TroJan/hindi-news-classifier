# -*- coding: utf-8 -*-

from __future__ import division

import codecs

from functools import partial
from math import exp
from os.path import dirname, join

def load_data_file(file_path):
    freq_dict = {}
    with codecs.open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            word, count = line.split(',')
            freq_dict[word] = int(count)

    return freq_dict

def find_likelihood_prob(word, freq_dict, total_count, vocab_count, alpha=1):
    prob = ((freq_dict.get(word, 0) + alpha) * 1.0) / (total_count + vocab_count)
    return prob


def get_category_variables(name):
    app_dir = dirname(__file__)
    data_file = join(app_dir, 'data', '{}.txt'.format(name))
    freq_dict = load_data_file(data_file)
    word_count = sum(freq_dict.values())
    return [freq_dict, word_count]


def classify_news(freq_input):
    scores = []
    outcome = None
    prob_word_business, prob_word_sports = 1, 1
    doc_count_business, doc_count_sports =  3, 1
    doc_count_total = doc_count_business + doc_count_sports
    prob_business = doc_count_business / doc_count_total
    prob_sports = doc_count_sports / doc_count_total
    freq_business, word_count_business = get_category_variables('business')
    freq_sports, word_count_sports = get_category_variables('sports')
    vocab_count_total = len(set(freq_business.keys() + freq_sports.keys()))
    find_likelihood_prob_business = partial(find_likelihood_prob,
        freq_dict=freq_business, total_count=word_count_business, vocab_count=vocab_count_total)
    find_likelihood_prob_sports = partial(find_likelihood_prob,
        freq_dict=freq_sports, total_count=word_count_sports, vocab_count=vocab_count_total)
    for word, count in freq_input.items():
        prob_word_business *= (find_likelihood_prob_business(word)**count)
        prob_word_sports *= (find_likelihood_prob_sports(word)**count)
    prob_word_business *= prob_business
    prob_word_sports *= prob_sports

    scores = [(exp(prob_word_business), 'business'), (exp(prob_word_sports), 'sports') ]
    scores.sort(reverse=True)
    outcome = scores[0][1] or None
    return outcome
