from django.conf.urls import include, url

from .views import *

urlpatterns = [

    url(r'all', (PreprocessAllView.as_view()), name='all_preprocess_view'),
    url(r'stem', (StemmingView.as_view()), name='stem_view'),
    url(r'stopwords', (StopWordsRemovalView.as_view()), name='stopwords_view'),
    url(r'', (TokenizeView.as_view()), name='tokenize_view'),

]
