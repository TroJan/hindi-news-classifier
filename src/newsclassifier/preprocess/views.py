from collections import OrderedDict

from hinditokenizer import *

from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from .forms import *


class TokenizeView(ListView):

    template_name = 'preprocess/tokenize.html'
    form_class = PreprocessForm

    def get(self, request, *args, **kwargs):
        form_obj = self.form_class(request.GET or None)
        no_hyphen_tokens, sentences, tokens, unique_tokens = [None] * 4
        hyphenTokenPresent = False
        # for finding unique tokens
        token_list = []
        unique_tokens_map = OrderedDict()

        if form_obj.is_valid():
            text = form_obj.cleaned_data.get('text')
            sentences = tokenize_sent(text)
            tokens = tokenize(text)

            no_hyphen_tokens, hyphenTokenPresent = remove_hyphenated_tokens(tokens, verbose_mode=True)

            # by default unique operation will be applied
            # on whole token set. However if any hyphenated token
            # is present, then it should be on `no_hyphen_tokens`
            if not hyphenTokenPresent:
                no_hyphen_tokens = None
                token_list = tokens
            else:
                token_list = no_hyphen_tokens

            # not using `set` to find unique tokens, since it does
            # not preserves the order
            for token in token_list:
                unique_tokens_map.setdefault(token, 0)
                unique_tokens_map[token]+=1

        return render(request, self.template_name, {
            'form': form_obj,
            'no_hyphen_tokens': no_hyphen_tokens,
            'sentences': sentences,
            'tokens': tokens,
            'unique_tokens': unique_tokens_map,
        })


class StemmingView(ListView):

    template_name = 'preprocess/stemming.html'
    form_class = PreprocessForm

    def get(self, request, *args, **kwargs):
        form_obj = self.form_class(request.GET or None)
        stem_map = OrderedDict()

        if form_obj.is_valid():
            text = form_obj.cleaned_data.get('text')
            tokens = tokenize(text)
            # remove hyphenated and duplicate hyphented words
            tokens = remove_hyphenated_tokens(tokens)

            for token in tokens:
                stem_map[token] = stem(token)

        return render(request, self.template_name, {
            'form': form_obj,
            'stem_words': stem_map
        })


class StopWordsRemovalView(ListView):

    template_name = 'preprocess/stopwords.html'
    form_class = PreprocessForm

    def get(self, request, *args, **kwargs):
        form_obj = self.form_class(request.GET or None)
        no_stopwords_tokens = None
        if form_obj.is_valid():
            text = form_obj.cleaned_data.get('text')
            tokens = tokenize(text)
            # remove hyphenated and duplicate hyphented words
            tokens = remove_hyphenated_tokens(tokens)
            stopwords = stopwords_list()

            no_stopwords_tokens = [token for token in tokens if token.encode('utf8') not in stopwords]

            stopwords_present = list(set(tokens) - set(no_stopwords_tokens))

        return render(request, self.template_name, {
            'form': form_obj,
            'no_stopwords_tokens': no_stopwords_tokens,
            'stopwords_present': stopwords_present,
        })

