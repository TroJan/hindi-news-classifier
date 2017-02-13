from collections import OrderedDict

from hinditokenizer import *

from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from newsclassifier.preprocess.utils import (
    preprocess_text_without_stemming,
    create_bag_of_words)

from .forms import *
from .utils import *


class NaiveBayesClassifier(ListView):

    template_name = 'classifier/naive.html'
    form_class = ClassificationTextForm

    def get(self, request, *args, **kwargs):
        form_obj = self.form_class(request.GET or None)
        outcome = None
        if form_obj.is_valid():
            text = form_obj.cleaned_data.get('text')
            tokens = preprocess_text_without_stemming(text)
            tokens = [stem(token) for token in tokens]
            freq_input = create_bag_of_words(tokens)
            outcome = classify_news(freq_input)


        return render(request, self.template_name, {
            'form': form_obj,
            'outcome': outcome
        })
