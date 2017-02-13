from django.conf.urls import include, url

from .views import *

urlpatterns = [

    url(r'naive', (NaiveBayesClassifier.as_view()), name='naive_classify_view'),

]
